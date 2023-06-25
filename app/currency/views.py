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


'''
1xx - info
2xx - success
200 - OK
201 - Created
202 - Accepted
204 - No content
3xx - redirect
301 - Moved Permanently
302 - Moved Temporarily
4xx - client error
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found
405 - Method Not Allowed
5xx - server failed
500 - Internal Server Error (Python code error)
'''


def status_code(request):
    print('sdasjdjk')
    response = HttpResponse(
        'DATA',
        status=200
    )
    return response
