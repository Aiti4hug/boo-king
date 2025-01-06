from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status', 'data_register')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']

# class CityListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = City
#         fields = ['city_name']

class HotelPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = ['hotel_image']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'room_price', 'room_type']

class RoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = '__all__'

class RatingListSerializer(serializers.ModelSerializer):
    profile = ProfileSimpleSerializer()

    class Meta:
        model = Rating
        fields = ['profile', 'hotel']

class HotelListSerializer(serializers.ModelSerializer):
    hotel_photo = HotelPhotoSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    year = serializers.DateField(format('%m-%d-%Y'))

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_photo', 'hotel_name', 'country', 'city',
                  'hotel_address', 'avg_rating', 'count_people', 'year']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()

class HotelSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name']

class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_owner = ProfileSimpleSerializer()
    hotel_photo = HotelPhotoSerializer(many=True, read_only=True)
    ratings = RatingListSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    year = serializers.DateField(format('%m-%d-%Y'))

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_photo', 'country', 'city',
                  'hotel_owner', 'hotel_video', 'hotel_address',
                  'ratings', 'avg_rating', 'count_people', 'description', 'year']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()


class BookingListSerializer(serializers.ModelSerializer):
    user = ProfileSimpleSerializer()
    hotel = HotelSimpleSerializer()

    class Meta:
        model = Booking
        fields = ['user', 'hotel']

class BookingDetailSerializer(serializers.ModelSerializer):
    user = ProfileSimpleSerializer()
    hotel = HotelListSerializer()
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = '__all__'

# class CityDetailSerializer(serializers.ModelSerializer):
#     hotels = HotelListSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = City
#         fields = ['city_name', 'hotels']


class RatingDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSimpleSerializer()

    class Meta:
        model = Rating
        fields = ['profile', 'hotel', 'hotel_stars', 'text', 'parent']