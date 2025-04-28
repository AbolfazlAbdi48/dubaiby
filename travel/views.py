from django.shortcuts import render
from django.views.generic import DetailView

from travel.models import Hotel, TravelCategory


# Create your views here.
def hotel_list_view(request):
    hotels = Hotel.objects.filter(active=True)
    categories = TravelCategory.objects.all()

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
