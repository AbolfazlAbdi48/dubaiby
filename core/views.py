from django.shortcuts import render
from django.views.generic import DetailView

from travel.models import Tour, Hotel


# Create your views here.
def home(request):
    tours = Tour.objects.all()
    hotels = Hotel.objects.all()

    context = {
        'tours': tours,
        'hotels': hotels
    }
    return render(request, 'core/home.html', context=context)


class TourDetailView(DetailView):
    model = Tour
    template_name = 'core/tour_detail.html'


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'core/hotel_detail.html'
