def foo(x, y=1):
    return x + 1


def foo1(x, y=1):
    return x + 1


# flake8, pylint
print(foo(5))
