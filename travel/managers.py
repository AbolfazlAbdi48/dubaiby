from django.db import models
from django.db.models import Q


class TourManager(models.Manager):
    def search_tours(self, user_query):
        """Search tours by title, description, keywords"""
        return self.get_queryset().filter(
            Q(title__icontains=user_query) |
            Q(description__icontains=user_query) |
            Q(keywords__icontains=user_query)
        )


class HotelManager(models.Manager):
    def search_hotels(self, user_query):
        """Search hotels by title, description, keywords"""
        return self.get_queryset().filter(
            Q(title__icontains=user_query) |
            Q(description__icontains=user_query) |
            Q(keywords__icontains=user_query)
        )


class FlightManager(models.Manager):
    def search_flight(self, user_query):
        """Search flights by title, description, keywords"""
        return self.get_queryset().filter(
            Q(airline__icontains=user_query) |
            Q(keywords__icontains=user_query)
        )


class ProviderManager(models.Manager):
    def search_providers(self, user_query):
        """Search flights by title, description, keywords"""
        return self.get_queryset().filter(
            Q(keywords__icontains=user_query)
        )
