from django_filters import FilterSet
from .models import Hotel, Room


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'hotel_name': ['exact'],
#             'hotel_address': ['exact'],
#             'country': ['exact'],
#             'city': ['exact'],
        }

class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_price': ['gt', 'lt']
        }