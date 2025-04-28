from django.shortcuts import render
from django.views.generic import DetailView

from travel.models import Hotel, TravelCategory, Tour


# Create your views here.
def hotel_list_view(request):
    hotels = Hotel.objects.filter(active=True)
    categories = TravelCategory.objects.filter(for_hotel=True)

    category = request.GET.get('category')
    if category:
        hotels = Hotel.objects.filter(active=True, categories__name__icontains=category)

    context = {
        'hotels': hotels,
        'categories': categories,
        'category': category,
    }
    return render(request, 'travel/hotel_list.html', context)


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'travel/hotel_detail.html'


def tour_list_view(request):
    tours = Tour.objects.filter(active=True)
    categories = TravelCategory.objects.filter(for_tour=True)

    category = request.GET.get('category')
    if category:
        tours = Tour.objects.filter(active=True, categories__name__icontains=category)

    context = {
        'tours': tours,
        'categories': categories,
        'category': category,
    }
    return render(request, 'travel/tour_list.html', context)


class TourDetailView(DetailView):
    model = Tour
    template_name = 'travel/tour_detail.html'
