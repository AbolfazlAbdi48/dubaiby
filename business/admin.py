from django.contrib import admin

from business.models import BusinessObj


# Register your models here.
@admin.register(BusinessObj)
class BusinessObjAdmin(admin.ModelAdmin):
    pass
