from django.shortcuts import render

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
