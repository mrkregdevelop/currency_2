from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2, validators=[])
    created = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=3)  # usd, eur
    source = models.CharField(max_length=68)


class Source(models.Model):
    name = models.CharField(max_length=64)
