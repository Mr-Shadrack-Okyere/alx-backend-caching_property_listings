# properties/views.py
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .utils import getallproperties  # use correct function

@cache_page(60 * 15)
def property_list(request):
    properties = getallproperties()  # <- correct call
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
