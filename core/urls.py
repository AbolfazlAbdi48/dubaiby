from django.urls import path
from .views import home, TourDetailView

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path("tours/<pk>", TourDetailView.as_view(), name="tour-detail"),
]
