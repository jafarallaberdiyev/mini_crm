from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import cloudinary.uploader
from .models import Student, Room, Booking
from .serializers import StudentSerializer, RoomSerializer, BookingSerializer, AvatarUploadSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['post'])
    def upload_avatar(self, request, pk=None):
        student = self.get_object()
        serializer = AvatarUploadSerializer(data=request.data)

        if serializer.is_valid():
            avatar_file = serializer.validated_data['avatar']

            try:
                # Загрузка в Cloudinary
                upload_result = cloudinary.uploader.upload(avatar_file)
                avatar_url = upload_result['secure_url']

                # Сохранение URL в базе данных
                student.avatar_url = avatar_url
                student.save()

                return Response(StudentSerializer(student).data)

            except Exception as e:
                return Response(
                    {'error': f'Ошибка загрузки файла: {str(e)}'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = Booking.objects.all()

        # Фильтрация по комнате
        room_id = self.request.query_params.get('room_id')
        if room_id:
            queryset = queryset.filter(room_id=room_id)

        # Фильтрация по студенту
        student_id = self.request.query_params.get('student_id')
        if student_id:
            queryset = queryset.filter(student_id=student_id)

        # Фильтрация по дате
        date = self.request.query_params.get('date')
        if date:
            queryset = queryset.filter(start_time__date=date)

        return queryset