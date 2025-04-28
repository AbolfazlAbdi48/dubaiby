from django.urls import path
from .views import hotel_list_view, HotelDetailView, tour_list_view, TourDetailView

app_name = 'travel'
urlpatterns = [
    path('hotels/', hotel_list_view, name='hotel-list'),
    path('hotels/<int:pk>/<str:title>', HotelDetailView.as_view(), name='hotel-detail'),
    path('tours/', tour_list_view, name='tour-list'),
    path('tours/<int:pk>/<str:title>', TourDetailView.as_view(), name='tour-detail'),
]
