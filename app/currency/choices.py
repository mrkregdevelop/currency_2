# CURRENCY_DOLLAR = 1
# CURRENCY_EURO = 2
# CURRENCY_CHOICES = [
#     (CURRENCY_DOLLAR, 'Dollar'),
#     (CURRENCY_EURO, 'Euro'),
# ]
from django.utils.translation import gettext_lazy as _
from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    USD = 1, _('Dollar')
    EUR = 2, _('Euro')
