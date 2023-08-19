from django.urls import path
from rest_framework.routers import DefaultRouter

from currency.api.views import (
    RateViewSet
)

app_name = 'currency_api'

router = DefaultRouter(trailing_slash=False)
router.register('rates/', RateViewSet, basename='rates')


urlpatterns = [
] + router.urls
