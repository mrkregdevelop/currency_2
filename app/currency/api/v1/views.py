from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from currency.api.v1.filters import RateFilter
from currency.api.v1.paginators import RatePagination
from currency.api.v1.serializers import RateSerializer
from currency.choices import RateCurrencyChoices
from currency.consts import LATEST_RATE_KEY
from currency.models import Rate, Source


# class RatesListApiView(generics.ListCreateAPIView):
#     queryset = Rate.objects.all().order_by('-created')
#     serializer_class = RateSerializer  # json -> obj, obj -> json
#     renderer_classes = (JSONRenderer, YAMLRenderer, XMLRenderer)
#
#
# class RateDetailApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all().order_by('-created')
#     serializer_class = RateSerializer  # json -> obj, obj -> json


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-id')
    serializer_class = RateSerializer  # json -> obj, obj -> json
    # renderer_classes = (JSONRenderer, YAMLRenderer, XMLRenderer)
    pagination_class = RatePagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = RateFilter
    ordering_fields = ('buy', 'sell', 'created')
    permission_classes = (AllowAny,)

    @action(methods=['GET'], detail=False, serializer_class=RateSerializer)
    def latest(self, request, *args, **kwargs):

        cached_data = cache.get(LATEST_RATE_KEY)

        if cached_data is not None:
            return Response(cached_data)

        sources = Source.objects.all()

        latest_rates = []
        for source_obj in sources:
            for currency in RateCurrencyChoices:
                rate = Rate.objects.filter(source=source_obj, currency=currency).order_by('-created').first()

                if rate is not None:
                    latest_rates.append(RateSerializer(instance=rate).data)

        cache.set(LATEST_RATE_KEY, latest_rates, 60 * 60 * 24 * 7)

        return Response(latest_rates)

