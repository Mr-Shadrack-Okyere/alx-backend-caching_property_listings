from django.core.cache import cache
from .models import Property

def getallproperties():
    # Try to get from cache
    queryset = cache.get('allproperties')
    if queryset is not None:
        return queryset

    # Fetch from database
    queryset = list(Property.objects.all())

    # Store in cache for 1 hour
    cache.set('allproperties', queryset, 3600)

    return queryset

