from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.school_map, name='school_map'),
]
