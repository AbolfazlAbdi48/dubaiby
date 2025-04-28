from django.urls import path
from .views import hotel_list_view, HotelDetailView

app_name = 'travel'
urlpatterns = [
    path('hotels/', hotel_list_view, name='hotel-list'),
    path('hotels/<int:pk>/<str:title>', HotelDetailView.as_view(), name='hotel-detail')
]
