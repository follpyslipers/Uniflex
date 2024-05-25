from django.urls import path
from . import views

urlpatterns = [
    path('daily-visitors/', views.daily_visitors, name='daily_visitors'),
    path('visitor-engagement/', views.visitor_engagement, name='visitor_engagement'),
]
