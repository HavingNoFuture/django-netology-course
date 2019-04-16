import time
import random

from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket

CACHE_TIMEOUT = 120

class TicketPageView(FormMixin, TemplateView):
    form_class = SearchTicket
    template_name = 'app/ticket_page.html'


    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    term = request.GET.get('term')

    cache_key = f'cities-{term}'
    cached = cache.get(cache_key)

    if cached is not None:
        return JsonResponse(cached, safe=False)

    if term:
        cities = City.objects.filter(name__icontains=term)
        results = [city.name for city in cities]
        cache.set(cache_key, results, CACHE_TIMEOUT)
    else:
        results = []

    return JsonResponse(results, safe=False)
