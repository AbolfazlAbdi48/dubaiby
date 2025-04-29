from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import ProviderProfile, ProviderLink
from django.contrib.contenttypes.models import ContentType


# Register your models here.
@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    search_fields = ['model']


class ProviderLinkInline(GenericTabularInline):
    model = ProviderLink
    extra = 1
    autocomplete_fields = ['content_type']


@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    # inlines = [ProviderLinkInline]


@admin.register(ProviderLink)
class ProviderLinkAdmin(admin.ModelAdmin):
    list_display = ('provider', 'label', 'link', 'content_object', 'created_at')
    search_fields = ('label', 'link')
    autocomplete_fields = ['content_type']
