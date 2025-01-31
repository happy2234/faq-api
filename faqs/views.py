from rest_framework import viewsets
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        if not (data := cache.get(cache_key)):
            data = self.serializer_class(self.get_queryset(), many=True, context={'request': request}).data
            cache.set(cache_key, data, 900)
        return Response(data)