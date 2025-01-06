from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'hotel_address', 'description')

# @register(City)
# class CityTranslationOptions(TranslationOptions):
#     fields = ('city_name',)