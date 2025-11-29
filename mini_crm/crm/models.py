from django.db import models
from django.utils import timezone


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar_url = models.URLField(max_length=1000, blank=True, null=True, verbose_name='URL аватара')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.name


class Room(models.Model):
    ROOM_TYPES = (
        ('LECTURE', 'Лекционная'),
        ('COMPUTER', 'Компьютерная'),
        ('CONFERENCE', 'Переговорная'),
        ('STUDIO', 'Студия'),
    )

    name = models.CharField(max_length=255, verbose_name='Название')
    capacity = models.PositiveIntegerField(verbose_name='Вместимость')
    type = models.CharField(max_length=50, choices=ROOM_TYPES, verbose_name='Тип')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings', verbose_name='Комната')
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Студент')
    start_time = models.DateTimeField(verbose_name='Время начала')
    end_time = models.DateTimeField(verbose_name='Время окончания')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        indexes = [
            models.Index(fields=['room', 'start_time', 'end_time']),
        ]
        ordering = ['start_time']

    def __str__(self):
        student_name = self.student.name if self.student else 'Группа'
        return f"{self.room.name} - {student_name} ({self.start_time:%d.%m.%Y %H:%M})"