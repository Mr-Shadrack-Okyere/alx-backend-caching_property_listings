# properties/views.py
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .utils import get_all_properties  # <- use the low-level cached function

@cache_page(60 * 15)  # cache the view for 15 minutes
def property_list(request):
    properties = get_all_properties()  # <- low-level cached queryset
    data = [
        {
            "id": prop.id,
            "title": prop.title,
            "description": prop.description,
            "price": float(prop.price),
            "location": prop.location,
            "created_at": prop.created_at.isoformat(),
        }
        for prop in properties
    ]
    return JsonResponse({"properties": data})
