from django.core.cache import cache
from .models import Property

def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all().values())
        cache.set('all_properties', properties, 3600)  # cache for 1 hour
    return properties
