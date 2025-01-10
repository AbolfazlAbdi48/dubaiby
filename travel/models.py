from django.db import models


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

    airline = models.CharField(max_length=100, verbose_name="شرکت هواپیمایی")
    airline_logo = models.ImageField(upload_to='airline_logos/', null=True, blank=True,
                                     verbose_name="لوگوی شرکت هواپیمایی")
    flight_number = models.CharField(max_length=100, verbose_name="شماره پرواز")
    travel_type = models.CharField(max_length=20, choices=TRAVEL_TYPE_CHOICES, verbose_name="نوع سفر")
    origin = models.CharField(max_length=100, verbose_name="مبدا")
    destination = models.CharField(max_length=100, verbose_name="مقصد")
    departure_date = models.DateTimeField(verbose_name="تاریخ پرواز")
    arrival_date = models.DateTimeField(verbose_name="تاریخ ورود")
    price_adult = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت بزرگسال")
    price_child = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت کودک")
    price_infant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت نوزاد")

    def __str__(self):
        return f"{self.airline} از {self.origin} به {self.destination}"
