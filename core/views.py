import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from openai import OpenAI
from travel.models import Tour, Hotel

client = OpenAI(
    api_key="FAKE",
    base_url="http://localhost:1337/v1"
)


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


@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        system_content = '''
            You are a helpful travel assistant specialized in Dubai.
            say in persian.
            show: heading and title with html tag <h4>, line break with tag <br>, text with tag <p>.
            فقط به سوالاتی که درباره دبی هست پاسخ بده و به سوالات متفرقه پاسخ بده:
             "من میتونم در زمینه سفر به دبی و فرصت های تجاری دبی راهنماییت کنم..."
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

            return JsonResponse({"reply": assistant_message}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    context = {}
    return render(request, 'core/chatbot.html', context=context)
