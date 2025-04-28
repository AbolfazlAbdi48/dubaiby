from django.contrib import admin
from .models import (
    FlightTicket,
    Hotel,
    HotelRoom,
    Image,
    Tour,
    TourDay,
    Provider, TravelCategory
)


# Register your models here.
class HotelRoomInline(admin.StackedInline):
    model = HotelRoom
    extra = 0


class TourDayInline(admin.StackedInline):
    model = TourDay
    extra = 0


@admin.register(FlightTicket)
class FlightTicketAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'departure_date', 'arrival_date', 'airline', 'active')
    list_filter = ('departure_date', 'arrival_date', 'travel_type')
    list_editable = ('active',)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'active')
    list_editable = ('active',)
    inlines = [
        HotelRoomInline
    ]


@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('get_thumbnail', '__str__')
    search_fields = ('hotel__title', 'tour__title')


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'active')
    search_fields = ('title', 'description')
    list_editable = ('active',)
    inlines = [
        TourDayInline
    ]


@admin.register(TourDay)
class TourDayAdmin(admin.ModelAdmin):
    pass


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'active')
    list_editable = ('active',)
    search_fields = ('provider', 'affiliate_link', 'hotel__title', 'tour__title', 'flight__airline')


@admin.register(TravelCategory)
class TravelCategoryAdmin(admin.ModelAdmin):
    pass
