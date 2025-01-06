from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()



urlpatterns = [
    path('', include(router.urls)),
    path('hotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('booking/', BookingListAPIView.as_view(), name='booking_list'),
    path('booking/<int:pk>/', BookingDetailAPIView.as_view(), name='booking_detail'),
    path('users/', ProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', ProfileDetailAPIView.as_view(), name='user_detail'),
    path('room/', RoomListAPIView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomDetailAPIVie.as_view(), name='room_detail'),
    path('rating/', RatingListAPIView.as_view(), name='rating_list'),
    path('rating/<int:pk>/', RatingDetailAPIView.as_view(), name='rating_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]