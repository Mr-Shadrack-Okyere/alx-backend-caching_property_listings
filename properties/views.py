from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .utils import getallproperties  # <- updated import

@cache_page(60 * 15)  # cache 15 minutes
def property_list(request):
    properties = getallproperties()  # <- call updated function
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
