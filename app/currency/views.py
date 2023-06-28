from django.http.response import HttpResponse
from django.shortcuts import render

from currency.models import Rate


def rate_list(request):
    '''
    MVTU
    V - view
    U - urls
    M - model
    T - template
    '''
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }
    return render(request, 'rate_list.html', context)


def test_template(request):
    name = request.GET.get('name')
    context = {
        'username': name
    }
    return render(request, 'test.html', context)



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
    response = HttpResponse(
        'DATA',
        status=200
    )
    return response
