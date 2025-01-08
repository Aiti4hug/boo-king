from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

STATUS_CHOICES = (
    ('client', 'client'),
    ('owner',  'owner')
)

class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(110)],
                                           null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    data_register = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    hotel_owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    hotel_address = models.CharField(max_length=50)
    hotel_video = models.FileField(upload_to='hotel_videos', null=True, blank=True)
    register_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.hotel_name} - {self.city}'

    def get_avg_rating(self):
        rating = self.ratings.all()
        if rating.exists():
            return round(sum(i.hotel_stars for i in rating) / rating.count(), 1)
        return 0

    def get_count_people(self):
        rating = self.ratings.all()
        if rating.exists():
            return rating.count()
        return 0


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    room_number = models.PositiveIntegerField()
    room_price = models.PositiveIntegerField()
    ROOM_CHOICES = (
        ('free', 'free'),
        ('booked', 'booked'),
        ('busy', 'busy')
    )
    status_room = models.CharField(choices=ROOM_CHOICES, max_length=30)
    ROOM_TYPE_CHOICES = (
        ('Single_Room', 'Single_Room'),
        ('Two_room', 'Two_room'),
        ('Three_room', 'Three_room'),
        ('Family', 'Family'),
    )
    room_type = models.CharField(choices=ROOM_TYPE_CHOICES, max_length=30)
    all_inclusive = models.BooleanField(default=False)

    def __str__(self):
        return f'room: {self.room_number}  -  Hotel:  {self.hotel}'

class HotelPhoto(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_photo', null=True, blank=True)
    hotel_image = models.ImageField(upload_to='hotel_images/')

    def __str__(self):
        return  f'{self.hotel}'

class RoomPhoto(models.Model):
    hotel = models.ForeignKey(Hotel,  on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    room_image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return f'{self.room}'

class Rating(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='ratings')
    hotel_stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    text = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.profile} - {self.hotel_stars}  -  {self.hotel}'

class Booking(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    CHOICES = (
        ('Canceled', 'Canceled'),
        ('Confirmed', 'Confirmed')
    )
    status_booking = models.CharField(choices=CHOICES, max_length=20)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.hotel}'
