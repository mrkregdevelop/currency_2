from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def debug():
    from time import sleep
    sleep(10)
    print('DEBUG\n' * 10)


@shared_task(
    autoretry_for=(ConnectionError,),
    retry_kwargs={'max_retries': 5}
)
def send_email_in_background(subject, body):
    raise ConnectionError

    from time import sleep
    sleep(10)

    recipient = settings.DEFAULT_FROM_EMAIL
    send_mail(
        subject,
        body,
        recipient,
        [recipient],
        fail_silently=False
    )
