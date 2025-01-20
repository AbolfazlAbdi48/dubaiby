from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import User


# Create your models here.
class ChatMessage(models.Model):
    user = models.ForeignKey(to=User, verbose_name=_('کاربر', ), on_delete=models.CASCADE, null=True, blank=True)
    user_message = models.TextField(verbose_name=_('پیام کاربر'))
    bot_message = models.TextField(verbose_name=_('پیام بات'))
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_message
