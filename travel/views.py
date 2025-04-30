from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.views.generic import DetailView

from affiliate_module.models import ProviderLink
from travel.models import Hotel, TravelCategory, Tour, Visa, FlightTicket


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hotel = self.object

        hotel_type = ContentType.objects.get_for_model(Hotel)

        provider_links = ProviderLink.objects.filter(
            content_type=hotel_type,
            object_id=hotel.id
        )

        context['provider_links'] = provider_links
        return context


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


def visa_list_view(request):
    visa_type = ContentType.objects.get_for_model(Visa)
    visa_links = ProviderLink.objects.filter(content_type=visa_type)

    context = {
        'visa_links': visa_links,
    }
    return render(request, 'travel/visa_list.html', context)


def flight_list_view(request):
    flight = ContentType.objects.get_for_model(FlightTicket)
    flights = ProviderLink.objects.filter(content_type=flight)

    context = {
        'flights': flights,
    }
    return render(request, 'travel/flight_list.html', context)
