from django.shortcuts import render
from .models import Building

def school_map(request):
    buildings = Building.objects.all()
    return render(request, 'map.html', {'buildings': buildings})
