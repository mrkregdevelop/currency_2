from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from currency.consts import LATEST_RATE_KEY
from currency.models import Rate


@receiver(post_save, sender=Rate)
def rate_post_save_clear_cache(created, *args, **kwargs):
    print(created)
    if created:
        print('receiver')
        cache.delete(LATEST_RATE_KEY)
