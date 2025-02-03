import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from openai import OpenAI

from core.models import ChatMessage
from travel.models import Tour, Hotel, Provider

client = OpenAI(
    api_key="FAKE",
    base_url="http://localhost:1337/v1"
)


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
        system_content = '''
            You are a helpful travel assistant specialized in Dubai.
            show: heading and title with html tag <h4>, line break with tag <br>, text with tag <p>.
            Only answer questions related to travel, hotels, flights, tours, and Dubai.
            من میتونم در زمینه سفر به دبی و فرصت های تجاری دبی راهنماییت کنم.
            به یوزر بگو که میتونه در سایت همه رزرو هارو انجام بده، ما بهترین تور ها، هتل ها اقامتگاه ها و
            پرواز هارو از dubaiby رزرو کنه.
            آخر هر پیام یه cta بزار که یوزر بازم ترغیب بشه و با چت بات چت کنه.
            برای رزرو یوزر رو به سایت دبی بای ارجاع بده:
            <a href="/">رزرو از دبی بای</a>
        '''

        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            if not user_message:
                return JsonResponse({"error": "Message is required"}, status=400)

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": system_content
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            )

            assistant_message = response.choices[0].message.content

            chat_message = ChatMessage(
                user_message=user_message,
                bot_message=assistant_message
            )
            if request.user.is_authenticated:
                chat_message.user = request.user
            chat_message.save()

            return JsonResponse({"reply": assistant_message}, status=200)

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
