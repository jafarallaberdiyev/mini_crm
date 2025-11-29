from django.contrib import admin
from .models import Student, Room, Booking

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'created_at']
    search_fields = ['name', 'email']
    list_filter = ['created_at']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'capacity', 'created_at']
    list_filter = ['type', 'created_at']
    search_fields = ['name']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['room', 'student', 'start_time', 'end_time', 'created_at']
    list_filter = ['room', 'start_time', 'created_at']
    search_fields = ['room__name', 'student__name']
    date_hierarchy = 'start_time'