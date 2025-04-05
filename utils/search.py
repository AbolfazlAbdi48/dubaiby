from travel.models import Hotel, Tour, FlightTicket
from django.db.models import Q


def search_across_models(user_input):
    keywords = user_input.lower().split()

    hotel_query = Q()
    tour_query = Q()
    flight_query = Q()

    for word in keywords:
        hotel_query |= Q(keywords__icontains=word)
        tour_query |= Q(keywords__icontains=word)
        flight_query |= Q(keywords__icontains=word)

    # search
    hotel_results = Hotel.objects.filter(hotel_query).distinct()
    tour_results = Tour.objects.filter(tour_query).distinct()
    flight_results = FlightTicket.objects.filter(flight_query).distinct()

    def serialize(queryset, fields):
        return [
            {field: getattr(obj, field, None) for field in fields}
            for obj in queryset
        ]

    hotels_data = serialize(hotel_results, ['id', 'title'])
    tours_data = serialize(tour_results, ['id', 'title'])
    flights_data = serialize(flight_results, ['id', 'origin', 'destination'])

    result = {
        "hotels": hotels_data,
        "tours": tours_data,
        "flights": flights_data,
    }

    return result
