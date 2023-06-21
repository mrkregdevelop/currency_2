from django.http.response import HttpResponse

from currency.models import Rate


def rate_list(request):
    results = []
    rates = Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, sell:{rate.sell}, buy:{rate.buy}, '
            f'created: {rate.created}, currency_type: {rate.currency_type}, source: {rate.source}<br>'
        )

    return HttpResponse(str(results))
