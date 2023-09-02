from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'

    def ready(self):
        from . import receivers


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
