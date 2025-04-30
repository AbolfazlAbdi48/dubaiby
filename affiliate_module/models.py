from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class ProviderProfile(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    profile_pic = models.ImageField(upload_to='providers/profile/', verbose_name=_('Profile'))
    about = models.TextField(verbose_name=_('About'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProviderLink(models.Model):
    provider = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name='links',
        verbose_name=_('Provider')
    )
    link = models.URLField(verbose_name=_('Link'))
    label = models.CharField(max_length=255, verbose_name=_('Label'))
    price = models.BigIntegerField(default=0, verbose_name=_('Price'))
    currency = models.CharField(max_length=20, default='AED', verbose_name=_('Currency'))

    # Generic relation to any model (Hotel, Tour, Flight, etc.)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.provider.title} - {self.label}"
