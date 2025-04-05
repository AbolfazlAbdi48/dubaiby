import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from core.models import ChatMessage
from travel.models import Tour, Hotel, Provider
from utils.gpt import gpt_request, SYSTEM_CONTENT
from utils.search import search_across_models


# Create your views here.
def home(request):
    tours = Tour.objects.filter(active=True)
    hotels = Hotel.objects.filter(active=True)
    flights = Provider.objects.filter(flight__isnull=False, flight__active=True)

    context = {
        'tours': tours,
        'hotels': hotels,
        'flights': flights
    }
    return render(request, 'core/home.html', context=context)


def contact_view(request):
    context = {}
    return render(request, 'core/contact.html', context=context)


class TourDetailView(DetailView):
    model = Tour
    template_name = 'core/tour_detail.html'


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'core/hotel_detail.html'


@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":

        try:
            # user prompt
            data = json.loads(request.body)
            user_message = data.get("message", "")
            if not user_message:
                return JsonResponse({"error": "Message is required"}, status=400)

            results = search_across_models(user_message)

            # gpt request for client
            gpt_response = gpt_request(SYSTEM_CONTENT, user_message, request.user.id)
            # save user prompt and gpt response
            chat_message = ChatMessage(
                user_message=user_message,
                bot_message=gpt_response
            )
            if request.user.is_authenticated:
                chat_message.user = request.user
            chat_message.save()

            return JsonResponse(
                {
                    "reply": 'gpt_response',
                    "results": results
                },
                status=200
            )

        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)}, status=500)

    messages = None
    if request.user.is_authenticated:
        messages = ChatMessage.objects.filter(user=request.user)
    context = {
        "messages": messages
    }
    return render(request, 'core/chatbot.html', context=context)
