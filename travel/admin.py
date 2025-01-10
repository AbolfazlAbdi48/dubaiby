from django.contrib import admin
from .models import (
    FlightTicket,
)


# Register your models here.
@admin.register(FlightTicket)
class FlightTicketAdmin(admin.ModelAdmin):
    pass
