from django.urls import path
from .views import home, contact_view, chatbot_view

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path("contact-us/", contact_view, name="contact-us"),
    path("chat/", chatbot_view, name="chatbot"),
]
