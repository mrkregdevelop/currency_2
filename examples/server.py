def hello(request):
    return b'Hello'


def world(request):
    return b'World'


urlpatterns = {
    '/hello/': hello,
    '/world/': world,
}


class Request():
    pass


def app(environ, start_response):
    path = environ['RAW_URI']
    view_func = urlpatterns.get(path)

    if view_func is None:
        data = b'Not Found'
        start_response("404 Not Found", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])

    data = view_func(Request())
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
