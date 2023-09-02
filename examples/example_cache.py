# from time import time
# from time import sleep
#
# CACHE = {}
#

'''
LEGB
L - local
E - enclosing
G - global
B - builtin
'''
from time import sleep, time


#
#
# def slow(n, a):
#     global CACHE
#
#     key = f'slow_{n}_{a}'
#
#     if key in CACHE:
#         return CACHE[key]
#
#     sleep(n)
#     result = n ** 2 + a
#     CACHE[key] = result
#
#     return result
#
#
# def slow2(n, a):
#     global CACHE
#
#     key = f'slow2_{n}_{a}'
#
#     if key in CACHE:
#         return CACHE[key]
#
#     sleep(n)
#     result = n ** 2 - a
#     CACHE[key] = result
#
#     return result
#
#
# start = time()
# print(slow(1, 23))
# print(slow(2, 3))
# print(slow2(1, 23))
# print(slow2(2, 3))
# print(f'Time: {time() - start}')
#
# print(CACHE)


def lru_cache(function):
    CACHE = {}

    def wrapper(*args, **kwargs):
        key = f'{function.__name__}::{args}::{kwargs}'
        if key in CACHE:
            return CACHE[key]

        result = function(*args, **kwargs)
        CACHE[key] = result

        return result

    return wrapper


@lru_cache
def foo(a):
    sleep(a)
    return 2


@lru_cache
def bar(a):
    sleep(a)
    return 4


@lru_cache
def slow(n, a):
    sleep(n)
    result = n ** 2 + a
    return result


start = time()
print(foo(1))
print(bar(2))
print(foo(1))
print(bar(2))
print(slow(2, 3))
print(slow(2, 3))

print(f'Time: {time() - start}')
