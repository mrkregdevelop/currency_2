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
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    class Meta:
        verbose_name = _('Rate')
        verbose_name_plural = _('Rates')


class Source(models.Model):
    '''
    OneToOne - X
    OneToMany - Y
    ManyToMany - X
    '''
    name = models.CharField(_('Name'), max_length=64)

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    name = models.CharField(_('Name'), max_length=128)
    reply_to = models.EmailField(_('Email'))
    subject = models.CharField(_('Subject'), max_length=128)
    body = models.CharField(_('Body'), max_length=1024)
