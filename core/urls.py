from django.urls import path
from .views import home, TourDetailView, HotelDetailView, chatbot_view

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path("chat/", chatbot_view, name="chatbot"),
    path("tours/<pk>", TourDetailView.as_view(), name="tour-detail"),
    path("hotels/<pk>", HotelDetailView.as_view(), name="hotel-detail"),
]
