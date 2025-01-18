from django.contrib import admin
from .models import (
    FlightTicket,
    Hotel,
    HotelRoom,
    Image,
    Tour,
    TourDay,
    Provider
)


# Register your models here.
@admin.register(FlightTicket)
class FlightTicketAdmin(admin.ModelAdmin):
    pass


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass


@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    pass


@admin.register(TourDay)
class TourDayAdmin(admin.ModelAdmin):
    pass


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass
