# Generated by Django 5.1.4 on 2025-01-06 06:25

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30, unique=True)),
                ('city_name_en', models.CharField(max_length=30, null=True, unique=True)),
                ('city_name_ru', models.CharField(max_length=30, null=True, unique=True)),
                ('city_name_de', models.CharField(max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(110)])),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('data_register', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('client', 'client'), ('owner', 'owner')], max_length=40)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=60)),
                ('hotel_name_en', models.CharField(max_length=60, null=True)),
                ('hotel_name_ru', models.CharField(max_length=60, null=True)),
                ('hotel_name_de', models.CharField(max_length=60, null=True)),
                ('country', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_de', models.TextField(null=True)),
                ('hotel_address', models.CharField(max_length=50)),
                ('hotel_address_en', models.CharField(max_length=50, null=True)),
                ('hotel_address_ru', models.CharField(max_length=50, null=True)),
                ('hotel_address_de', models.CharField(max_length=50, null=True)),
                ('hotel_video', models.FileField(blank=True, null=True, upload_to='hotel_videos')),
                ('register_date', models.DateField(auto_now_add=True, null=True)),
                ('hotel_stars', models.IntegerField()),
                ('hotel_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('city', models.ManyToManyField(related_name='hotels', to='ohio.city')),
                ('hotel_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HotelPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_image', models.ImageField(upload_to='hotel_images/')),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_photo', to='ohio.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_stars', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('text', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='ohio.hotel')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ohio.rating')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.PositiveIntegerField()),
                ('room_price', models.PositiveIntegerField()),
                ('status_room', models.CharField(choices=[('free', 'free'), ('booked', 'booked'), ('busy', 'busy')], max_length=30)),
                ('room_type', models.CharField(choices=[('Single_Room', 'Single_Room'), ('Two_room', 'Two_room'), ('Three_room', 'Three_room'), ('Family', 'Family')], max_length=30)),
                ('all_inclusive', models.BooleanField(default=False)),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ohio.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('status_booking', models.CharField(choices=[('Canceled', 'Canceled'), ('Confirmed', 'Confirmed')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ohio.hotel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ohio.room')),
            ],
        ),
        migrations.CreateModel(
            name='RoomPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_image', models.ImageField(upload_to='room_images/')),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ohio.hotel')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ohio.room')),
            ],
        ),
    ]
