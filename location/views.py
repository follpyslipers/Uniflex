from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render
from .models import Location

def location_list(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Check if it's an AJAX request for live filtering
        query = request.GET.get('q')
        page = request.GET.get('page', 1)  # Get the current page number from the request
        locations = Location.search(query) if query else Location.objects.all()

        # Pagination
        paginator = Paginator(locations, 6)  # 6 locations per page
        try:
            locations_page = paginator.page(page)
        except PageNotAnInteger:
            locations_page = paginator.page(1)
        except EmptyPage:
            locations_page = paginator.page(paginator.num_pages)

        location_data = [
            {
                'id': location.id,
                'name': location.name,
                'google_link': location.google_link
            } for location in locations_page
        ]
        return JsonResponse({
            'locations': location_data,
            'has_next': locations_page.has_next(),
            'has_previous': locations_page.has_previous(),
            'current_page': locations_page.number,
            'total_pages': paginator.num_pages,
        })
    else:  # Render the initial page
        locations = Location.objects.all()
        paginator = Paginator(locations, 6)  # 6 locations per page
        page = request.GET.get('page', 1)
        try:
            locations_page = paginator.page(page)
        except PageNotAnInteger:
            locations_page = paginator.page(1)
        except EmptyPage:
            locations_page = paginator.page(paginator.num_pages)

        # If an ID is passed in the query parameters, filter locations
        location_id = request.GET.get('id')
        if location_id:
            locations = locations.filter(id=location_id)

        return render(request, 'location_list.html', {
            'locations': locations_page,
            'paginator': paginator,
            'page_obj': locations_page,
        })
