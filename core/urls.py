from django.urls import path
from .views import home, contact_view, chatbot_view, dubai_life_view, dubai_business_view

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path("contact-us/", contact_view, name="contact-us"),
    path("chat/", chatbot_view, name="chatbot"),
    path("life/", dubai_life_view, name="dubai-life"),
    path("business/", dubai_business_view, name="dubai-business"),
]
