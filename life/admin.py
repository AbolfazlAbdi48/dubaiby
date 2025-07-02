from django.contrib import admin

from life.models import LifeObj


# Register your models here.
@admin.register(LifeObj)
class LifeObjAdmin(admin.ModelAdmin):
    pass
