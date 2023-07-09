from django.db import models
from django.utils.translation import gettext_lazy as _

from currency.choices import RateCurrencyChoices


class Rate(models.Model):
    buy = models.DecimalField(_('Buy'), max_digits=6, decimal_places=2)
    sell = models.DecimalField(_('Sell'), max_digits=6, decimal_places=2, validators=[])
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        _('Currency'),
        choices=RateCurrencyChoices.choices,
        # default=1
        default=RateCurrencyChoices.USD  # correct
    )  # if field contains choices (currency), then hr = object.get_<field_name>_display(), object.get_currency_display()
    source = models.CharField(_('Source'), max_length=68)

    class Meta:
        verbose_name = _('Rate')
        verbose_name_plural = _('Rates')


class Source(models.Model):
    name = models.CharField(_('Name'), max_length=64)

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')
