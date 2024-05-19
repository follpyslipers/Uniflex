from django.urls import path
from .views import location_list

app_name = 'location'

urlpatterns = [
    path('', location_list, name='location_list'),
]
