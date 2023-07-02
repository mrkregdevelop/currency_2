from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from currency.forms import RateForm
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


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)

        if form.is_valid():
            form.save()  # 1. get validated data, save Rate.objects.create(**validata_data)
            return HttpResponseRedirect('/rate/list/')

    elif request.method == 'GET':  # 1
        form = RateForm()

    context = {
        'form': form
    }
    return render(request, 'rate_create.html', context)


def rate_details(request, pk):
    rate = get_object_or_404(Rate, pk=pk)
    context = {
        'rate': rate
    }
    return render(request, 'rate_details.html', context)



def rate_update(request, pk):
    """
    BAD /rate/update/?id=12
    GOOD /rate/update/12/
    """
    # try:
    #     rate = Rate.objects.get(id=pk)
    # except Rate.DoesNotExist:
    #     raise Http404('Object does not exist')

    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)

        if form.is_valid():
            form.save()  # 1. get validated data, instance=validated_data, instance.save()
            return HttpResponseRedirect('/rate/list/')

    elif request.method == 'GET':  # 1
        form = RateForm(instance=rate)

    context = {
        'form': form
    }
    return render(request, 'rate_update.html', context)


def rate_delete(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'GET':
        context = {
            'object': rate
        }
        return render(request, 'rate_delete.html', context)
    elif request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')



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


@csrf_exempt
def request_method(request):
    '''
    1. GET - Client wants to get smth form server (retrieve)
    http://0.0.0.0:8000/rate/create/ ?buy=0.05&sell=0.03

    2. POST - Client wants to push smth to server (create)
    http://0.0.0.0:8000/rate/create/

    buy=0.05&sell=0.03

    3. PUT - Client wants to update record (update) buy=0.05&sell=0.03

    4. PATCH - Client wants to update record partially (partial update) buy=0.05 or sell=0.03

    5. DELETE - Client wants to delete record (delete)

    6. OPTIONS - Client wants to know request methods (list methods)

    7. HEAD (GET) - Client wants to know info about response (describe)

    CRUD

    C - POST (create)
    R - GET (read)
    U - PUT/PATCH (update)
    D - DELETE (delete)

    HTML - GET, POST
    '''

    if request.method == 'GET':
        message = 'Render Client Form'
    elif request.method == 'POST':
        message = 'Validate form data'

    return HttpResponse(message)
