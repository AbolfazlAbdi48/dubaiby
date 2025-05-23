from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from travel.managers import TourManager, HotelManager, FlightManager, ProviderManager


# Create your models here.
class TravelCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('category'))
    description = models.TextField(verbose_name=_('description'))
    image = models.ImageField(null=True, blank=True, upload_to='categories/travel/', verbose_name=_('تصویر'))
    for_hotel = models.BooleanField(default=True, verbose_name=_('For Hotel'))
    for_tour = models.BooleanField(default=True, verbose_name=_('For tour'))
    for_flight = models.BooleanField(default=True, verbose_name=_('For flight'))
    for_visa = models.BooleanField(default=True, verbose_name=_('For flight'))
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subcategories',
        verbose_name=_('parent')
    )

    class Meta:
        verbose_name = _('دسته بندی')
        verbose_name_plural = _('5. دسته بندی ها')

    def __str__(self):
        return self.name


class FlightTicket(models.Model):
    TRAVEL_TYPE_CHOICES = [
        ('ECONOMY', 'اکونومی'),
        ('PREMIUM_ECONOMY', 'پرمیوم اکونومی'),
        ('BUSINESS', 'بیزینس'),
        ('PREMIUM_BUSINESS', 'پرمیوم بیزینس'),
        ('FIRST', 'فرست'),
        ('PREMIUM_FIRST', 'پرمیوم فرست')
    ]

    airline = models.CharField(max_length=100, verbose_name=_("شرکت هواپیمایی"))
    airline_logo = models.ImageField(upload_to='airline_logos/', null=True, blank=True,
                                     verbose_name=_("لوگوی شرکت هواپیمایی"))
    flight_number = models.CharField(max_length=100, verbose_name=_("شماره پرواز"))
    travel_type = models.CharField(max_length=20, choices=TRAVEL_TYPE_CHOICES, verbose_name=_("نوع سفر"))
    origin = models.CharField(max_length=100, verbose_name=_("مبدا"))
    destination = models.CharField(max_length=100, verbose_name=_("مقصد"))
    departure_date = models.DateTimeField(verbose_name=_("تاریخ پرواز"))
    arrival_date = models.DateTimeField(verbose_name=_("تاریخ ورود"))
    price_adult = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("قیمت بزرگسال"))
    price_child = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("قیمت کودک"))
    price_infant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("قیمت نوزاد"))
    currency = models.CharField(max_length=20, null=True, verbose_name=_('واحد پول'))
    active = models.BooleanField(verbose_name=_('فعال/غیرفعال'), default=True)
    keywords = models.TextField(verbose_name=_('کلمات کلیدی'), null=True, blank=True)
    categories = models.ManyToManyField(
        to=TravelCategory,
        related_name='flight_categories',
        verbose_name=_('categories')

    )

    class Meta:
        verbose_name = 'پرواز'
        verbose_name_plural = '1. پرواز ها'

    objects = FlightManager()

    def __str__(self):
        return f"{self.airline} از {self.origin} به {self.destination}"


class Hotel(models.Model):
    image = models.ImageField(verbose_name=_('تصویر اصلی'), upload_to='hotels/')
    image_cover = models.ImageField(verbose_name=_('تصویر کاور'), upload_to='hotels/', null=True, blank=True)
    # ai_summary = models.TextField(verbose_name=_('خلاصه هوش مصنوعی'), null=True, blank=True)
    title = models.CharField(verbose_name=_('عنوان هتل'), max_length=200)
    location = models.CharField(verbose_name=_('لوکیشن'), max_length=200)
    location_url = models.CharField(verbose_name=_('آدرس گوگل مپ'), null=True, max_length=200)
    location_img = models.ImageField(verbose_name=_('تصویر لوکیشن'), upload_to='hotels/loc/', null=True, blank=True)
    rating = models.DecimalField(verbose_name=_('امتیاز'), max_digits=3, decimal_places=0)
    # TODO: add amenities for hotel
    description = models.TextField(verbose_name=_("توضیحات"))
    active = models.BooleanField(verbose_name=_('فعال/غیرفعال'), default=True)
    keywords = models.TextField(verbose_name=_('کلمات کلیدی'), null=True, blank=True)
    categories = models.ManyToManyField(
        to=TravelCategory,
        related_name='hotel_categories',
        verbose_name=_('categories')

    )

    class Meta:
        verbose_name = 'هتل'
        verbose_name_plural = '2. هتل ها'

    objects = HotelManager()

    def get_min_price(self):
        return self.rooms.first()

    def get_replaced_title(self):
        return self.title.replace(' ', '-')

    def get_absolute_url(self):
        return reverse('travel:hotel-detail', args=[self.id, self.get_replaced_title()])

    def __str__(self):
        return self.title


class Image(models.Model):
    hotel = models.ForeignKey(Hotel, verbose_name=_('هتل'), related_name='hotel_images', on_delete=models.CASCADE,
                              null=True, blank=True)
    tour = models.ForeignKey(to='Tour', verbose_name=_('تور'),
                             related_name='tour_images', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(verbose_name=_('تصویر'), upload_to='images/')

    def get_thumbnail(self):
        return format_html(f"<img width=100 height=75 style='border-radius: 5px;' src='{self.image.url}'>")

    get_thumbnail.short_description = "تصویر"

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = '4. تصاویر'

    def __str__(self):
        if self.hotel:
            return f"{self.hotel.title} hotel"
        elif self.tour:
            return f"{self.tour.title} tour"
        return "Image"


class HotelRoom(models.Model):
    title = models.CharField(verbose_name=_('عنوان'), max_length=200, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, verbose_name=_('هتل'), related_name='rooms', on_delete=models.CASCADE)
    meal_plan = models.CharField(verbose_name=_('وعده غذایی'), max_length=100)
    price_per_night = models.DecimalField(verbose_name=_('قیمت هر شب'), max_digits=10, decimal_places=0)
    currency = models.CharField(max_length=20, null=True, verbose_name=_('واحد پول'))
    description = models.TextField(verbose_name=_('توضیحات'), null=True, blank=True)
    image = models.ImageField(verbose_name=_('تصویر کاور'), upload_to='hotels/', null=True, blank=True)

    class Meta:
        verbose_name = 'اتاق هتل'
        verbose_name_plural = '2.1 اتاق ها'
        ordering = ('price_per_night',)

    def __str__(self):
        return f"{self.hotel.title} - {self.title}"


class Tour(models.Model):
    image = models.ImageField(verbose_name=_('تصویر'), upload_to='tours/images/')
    title = models.CharField(verbose_name=_('عنوان'), max_length=200)
    summary = models.CharField(verbose_name=_('خلاصه'), max_length=200)
    # ai_summary = models.TextField(verbose_name=_('خلاصه هوش مصنوعی'), null=True, blank=True)
    description = models.TextField(verbose_name=_('توضیحات'))
    # accommodation = models.CharField(verbose_name=_('اقامت'), max_length=200)
    # transport_text = models.CharField(verbose_name=_('حمل و نقل (متن)'), null=True, blank=True, max_length=200)
    # transport_ticket = models.ForeignKey(to='FlightTicket', verbose_name=_('حمل و نقل (بلیط پرواز)'),
    #                                      on_delete=models.SET_NULL,
    #                                      null=True, blank=True)
    # meals = models.CharField(verbose_name=_('وعده های غذایی'), max_length=200)
    start_time = models.DateTimeField(verbose_name=_('زمان شروع'))
    end_time = models.DateTimeField(verbose_name=_('زمان پایان'))
    price_per_person = models.DecimalField(verbose_name=_('قیمت به ازای هر نفر'), max_digits=10, decimal_places=0)
    currency = models.CharField(max_length=20, null=True, verbose_name=_('واحد پول'))
    active = models.BooleanField(verbose_name=_('فعال/غیرفعال'), default=True)
    keywords = models.TextField(verbose_name=_('کلمات کلیدی'), null=True, blank=True)
    categories = models.ManyToManyField(
        to=TravelCategory,
        related_name='tour_categories',
        verbose_name=_('categories')

    )

    class Meta:
        verbose_name = 'تور'
        verbose_name_plural = '3. تور ها'

    objects = TourManager()

    def get_replaced_title(self):
        return self.title.replace(' ', '-')

    def get_absolute_url(self):
        return reverse('travel:tour-detail', args=[self.id, self.get_replaced_title()])

    def __str__(self):
        return self.title


class TourDay(models.Model):
    day = models.CharField(verbose_name=_('روز'), max_length=200)
    summary = models.TextField(verbose_name=_('خلاصه'))
    image = models.ImageField(verbose_name=_('تصویر-Optional'), upload_to='tours/images', null=True, blank=True)
    tour = models.ForeignKey(to='Tour', verbose_name=_('تور'),
                             related_name='tour_days', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'برنامه تور'
        verbose_name_plural = '3.1 برنامه تور ها'

    def __str__(self):
        return f"{self.tour.title} - {self.day}"


class Visa(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    about = models.CharField(max_length=255, verbose_name=_('About'))
    categories = models.ManyToManyField(
        to=TravelCategory,
        related_name='visa_categories',
        verbose_name=_('categories')
    )
    keywords = models.TextField(verbose_name=_('Keywords'), null=True)

    class Meta:
        verbose_name = 'ویزا'
        verbose_name_plural = '6. ویزا'

    def __str__(self):
        return self.title
