# students = 'STRING'  # iterable
# students_iterator = students.__iter__()  # iterator object
#
# print(id(students))
# print(id(students_iterator))

# while True:
#     try:
#         print(students_iterator.__next__())
#     except StopIteration:
#         break


# for student in students:
#     print(student)

# gen = [i for i in 'STRING']
# gen = {i for i in 'STRING'}  # set
# gen = {i: i for i in 'STRING'}  # dict
# gen = (i for i in 'STRING')
#
# for i in gen:
#     print(i)
#
# for i in gen:
#     print(i)

'''map, filter'''
from contextlib import suppress, contextmanager

# def square():
#     counter = 0
#     while True:
#         print('GEN')
#         yield counter ** 2
#         counter += 1
#
#         if counter == 10:
#             return None
#
#
# s = square()
# s1 = square()
#
# for i in s:
#     print(i)

# class Browser:
#     '''250Mb'''
#     def __init__(self):
#         pass
#
#     def start(self):
#         pass
#
#
# browsers = (Browser() for i in range(10))
#
# for browser in browsers:
#     browser.start()

'''1Gb -> 10 Browser'''

# with open('Dockerfile') as file:
#     # for raw in file:
#     #     pass
#     print(next(file))
#     print(file.__next__())
#     print(file.__next__())


'''
+ - __add__
== - __eq__

__enter__
__exit__
'''


# class Connection:
#     def open(self):
#         print('OPEN')
#         return 'CONNECTION'
#
#     def close(self):
#         print('CLOSE')
#
#     def __enter__(self):
#         return self.open()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.close()
#
#
# c = Connection()
#
# with Connection() as obj:
#     print(obj)
#     1 + '1'


# try:
#     obj = c.open()
#     print(obj)
#     1 + '1'
# finally:
#     c.close()


# class Suppress:
#     def __init__(self, exc_type):
#         self.exc_type = exc_type
#
#     def __enter__(self):
#         pass
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return exc_type is not None and issubclass(exc_type, self.exc_type)
#
#
# @contextmanager
# def Suppress2(exc_type):
#     try:
#         yield None
#     finally:
#         pass
#
#
# with Suppress(TypeError):
#     1 + '1'
#
#
# with Suppress(TypeError):
#     1 + '1'

from functools import wraps
from time import sleep, time


def timeit(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()

        result = func(*args, **kwargs)

        end = time()
        print(f'Time: {end - start}')

        return result

    return wrapper


# class timeit2:
#     def __init__(self, function):
#         self.function = function
#
#     def __call__(self, *args, **kwargs):
#         start = time()
#
#         result = self.function(*args, **kwargs)
#
#         end = time()
#         print(f'Time: {end - start}')
#
#         return result


@timeit
def foo(a, b):
    '''
    Sleeps for 1 second

    :param a:
    :param b:
    :return:
    '''
    sleep(1)
    result = 1
    1 + '1'
    return result


# foo = timeit(1)(foo)

print(foo.__name__)
print(foo.__doc__)
print(foo.__module__)
foo(1, 2)

# print(foo(1, 2))
# print(foo(1, 2))


# @timeit
# def bar():
#     sleep(2)
#     result = 2
#     return result
#
#
# # bar = timeit(bar)
#
# bar()
# bar()

from django.views.decorators.http import require_http_methods
