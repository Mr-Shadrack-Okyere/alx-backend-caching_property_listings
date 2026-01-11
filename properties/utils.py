# properties/utils.py
from django.core.cache import cache
from .models import Property

def getallproperties():
    # Check Redis cache first
    cached = cache.get('allproperties')
    if cached is not None:
        return cached

    # Fetch from DB if cache miss
    queryset = list(Property.objects.all())

    # Store in cache for 1 hour
    cache.set('allproperties', queryset, 3600)

    return queryset
