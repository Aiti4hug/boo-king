from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

class HotelPhotoInline(admin.TabularInline):
    model = HotelPhoto
    extra = 2

class RoomInline(admin.TabularInline):
    model = Room
    extra = 2

class RoomPhotoInline(admin.TabularInline):
    model = RoomPhoto
    extra = 2

@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    inlines = [HotelPhotoInline,RoomInline , RoomPhotoInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

# @admin.register(City)
# class CityAdmin(TranslationAdmin):
#     class Media:
#         js = (
#             'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }

admin.site.register(Profile)
admin.site.register(Rating)
admin.site.register(Booking)
