from rest_framework import serializers
from django.utils import timezone
from .models import Student, Room, Booking


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'phone', 'email', 'avatar_url', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'capacity', 'type', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class BookingSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.name', read_only=True)
    room_name = serializers.CharField(source='room.name', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'room', 'room_name', 'student', 'student_name', 'start_time', 'end_time', 'created_at',
                  'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        room = data.get('room')

        if not start_time or not end_time:
            return data

        # Проверка, что время окончания больше времени начала
        if end_time <= start_time:
            raise serializers.ValidationError({
                "end_time": "Время окончания бронирования должно быть позже времени начала."
            })

        # Проверка, что бронирование не в прошлом
        if start_time < timezone.now():
            raise serializers.ValidationError({
                "start_time": "Нельзя создавать бронирования в прошлом."
            })

        # Проверка на пересечения
        overlapping_bookings = Booking.objects.filter(
            room=room,
            start_time__lt=end_time,
            end_time__gt=start_time,
        )

        # Исключаем текущую запись при обновлении
        if self.instance:
            overlapping_bookings = overlapping_bookings.exclude(pk=self.instance.pk)

        if overlapping_bookings.exists():
            raise serializers.ValidationError({
                "non_field_errors": ["Комната уже забронирована на это время. Выберите другое время."]
            })

        return data


class AvatarUploadSerializer(serializers.Serializer):
    avatar = serializers.ImageField()