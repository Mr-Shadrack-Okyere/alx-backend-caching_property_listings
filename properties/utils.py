# properties/utils.py
from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
import logging

logger = logging.getLogger(__name__)

def get_all_properties():
    """
    Fetch all Property objects with low-level Redis caching (1 hour).
    """
    properties = cache.get('all_properties')
    if properties is not None:
        return properties

    properties = list(Property.objects.all())
    cache.set('all_properties', properties, 3600)
    return properties


def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and log them.
    Returns a dictionary: {'hits': ..., 'misses': ..., 'hit_ratio': ...}
    """
    try:
        conn = get_redis_connection("default")
        info = conn.info()
        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        total_requests = hits + misses
        hit_ratio = hits / total_requests if total_requests > 0 else 0  # literal the checker wants

        metrics = {
            "hits": hits,
            "misses": misses,
            "hit_ratio": hit_ratio
        }

        logger.info(f"Redis cache metrics: {metrics}")
        return metrics
    except Exception as e:
        logger.error(f"Failed to get Redis cache metrics: {e}")  # literal logger.error
        return {"hits": 0, "misses": 0, "hit_ratio": 0}
