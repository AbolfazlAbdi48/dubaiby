from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
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

    def __str__(self):
        return f"{self.airline} از {self.origin} به {self.destination}"


class Hotel(models.Model):
    image = models.ImageField(verbose_name=_('تصویر اصلی'), upload_to='hotels/')
    title = models.CharField(verbose_name=_('عنوان هتل'), max_length=200)
    location = models.CharField(verbose_name=_('لوکیشن'), max_length=200)
    rating = models.DecimalField(verbose_name=_('امتیاز'), max_digits=3, decimal_places=2)
    amenities = models.TextField(verbose_name=_('امکانات'))
    description = models.TextField(verbose_name=_("توضیحات"))

    def __str__(self):
        return self.title


class Image(models.Model):
    hotel = models.ForeignKey(Hotel, verbose_name=_('هتل'), related_name='hotel_images', on_delete=models.CASCADE,
                              null=True, blank=True)
    tour = models.ForeignKey(to='Tour', verbose_name=_('تور'),
                             related_name='tour_images', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(verbose_name=_('تصویر'), upload_to='images/')

    def __str__(self):
        if self.hotel:
            return f"{self.hotel.title} - hotel"
        return f"{self.tour.title} - tour"


class HotelRoom(models.Model):
    title = models.CharField(verbose_name=_('عنوان'), max_length=200, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, verbose_name=_('هتل'), related_name='rooms', on_delete=models.CASCADE)
    meal_plan = models.CharField(verbose_name=_('وعده غذایی'), max_length=100)
    price_per_night = models.DecimalField(verbose_name=_('قیمت هر شب'), max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name=_('توضیحات'), null=True, blank=True)

    def __str__(self):
        return f"{self.hotel.title} - {self.title}"


class Tour(models.Model):
    image = models.ImageField(verbose_name=_('تصویر'), upload_to='tours/images/')
    title = models.CharField(verbose_name=_('عنوان'), max_length=200)
    summary = models.CharField(verbose_name=_('خلاصه'), max_length=200)
    description = models.TextField(verbose_name=_('توضیحات'))
    accommodation = models.CharField(verbose_name=_('اقامت'), max_length=200)
    transport_text = models.CharField(verbose_name=_('حمل و نقل (متن)'), null=True, blank=True, max_length=200)
    transport_ticket = models.ForeignKey(to='FlightTicket', verbose_name=_('حمل و نقل (بلیط پرواز)'),
                                         on_delete=models.SET_NULL,
                                         null=True, blank=True)
    meals = models.CharField(verbose_name=_('وعده های غذایی'), max_length=200)
    start_time = models.DateTimeField(verbose_name=_('زمان شروع'))
    end_time = models.DateTimeField(verbose_name=_('زمان پایان'))
    price_per_person = models.DecimalField(verbose_name=_('قیمت به ازای هر نفر'), max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
