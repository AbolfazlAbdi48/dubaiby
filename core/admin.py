from django.contrib import admin

from core.models import ChatMessage


# Register your models here.
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    pass
