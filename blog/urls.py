from django.urls import path
from .views import blog_view, BlogDetailView

app_name = 'blog'
urlpatterns = [
    path('', blog_view, name='blog-list'),
    path('<int:pk>/<str:title>', BlogDetailView.as_view(), name='blog-detail'),
]
