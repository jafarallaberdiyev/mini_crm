from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, RoomViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]