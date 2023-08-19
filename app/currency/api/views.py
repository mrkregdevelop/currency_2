from rest_framework import generics, viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer

from currency.api.serializers import RateSerializer
from currency.models import Rate


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
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer  # json -> obj, obj -> json
    renderer_classes = (JSONRenderer, YAMLRenderer, XMLRenderer)
