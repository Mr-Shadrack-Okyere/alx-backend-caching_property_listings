# properties/utils.py
from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Fetch all Property objects with low-level Redis caching.
    Cached for 1 hour (3600 seconds).
    """
    # Try to get cached queryset
    properties = cache.get('all_properties')
    if properties is not None:
        return properties

    # Fetch from DB if cache miss
    properties = list(Property.objects.all())

    # Store in Redis cache for 1 hour
    cache.set('all_properties', properties, 3600)

    return properties
