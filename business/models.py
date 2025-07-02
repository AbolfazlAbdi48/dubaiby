from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class BusinessObj(models.Model):
    image = models.ImageField(verbose_name=_('Thumbnail'), upload_to='business/images/')
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    summary = models.CharField(verbose_name=_('Summary'), max_length=200)
    # ai_summary = models.TextField(verbose_name=_('خلاصه هوش مصنوعی'), null=True, blank=True)
    description = models.TextField(verbose_name=_('Description'))
    price = models.DecimalField(verbose_name=_('Min Price'), null=True, blank=True, max_digits=10, decimal_places=0)
    currency = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Currency'))
    active = models.BooleanField(verbose_name=_('فعال/غیرفعال'), default=True)
    keywords = models.TextField(verbose_name=_('کلمات کلیدی'), null=True, blank=True)

    class Meta:
        verbose_name_plural = _('1. Business Objects')
        verbose_name = _('1. Business Object')

    def get_replaced_title(self):
        return self.title.replace(' ', '-')

    def __str__(self):
        return self.title
