# from time import sleep, time
# from threading import Thread, current_thread
#
#
# def slow(n):
#     print(current_thread())
#     sleep(n)
#
#
# start = time()
#
# threads = []
#
# for t in range(1, 11):
#     th1 = Thread(target=slow, args=[t])
#     threads.append(th1)
#     th1.start()
#
# print(current_thread())
# for th in threads:
#     th.join()
#
# print(f'Execution time: {time() - start}')
# from threading import Thread
# from time import time
#
# import requests
#
# urls = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://meta.wikimedia.org/wiki/Wikipedia/uk',
#     'https://itc.ua/tag/wikipedia/'
# ] * 20
#
# start = time()
#
#
# def foo(url):
#     response = requests.get(url)
#     print(response.status_code)
#
#
# threads = []
# for url in urls:
#     th = Thread(target=foo, args=[url])
#     threads.append(th)
#     th.start()
#
#
# for th in threads:
#     th.join()
#
# print(f'Execution time: {time() - start}')

# from threading import Thread
# from time import time
#
# # Global Interpreter Lock
# def countdown(n):
#     while n:
#         n -= 1
#
#
# start = time()
#
# th1 = Thread(target=countdown, args=[250_000_000])
# th2 = Thread(target=countdown, args=[250_000_000])
#
# th1.start()
# th2.start()
#
# th1.join()
# th2.join()
#
# print(f'Execution time: {time() - start}')


# from multiprocessing import Process, current_process
# from time import time
#
#
# # Global Interpreter Lock
# def countdown(n):
#     print(current_process())
#     while n:
#         n -= 1
#
#
# if __name__ == '__main__':
#     start = time()
#
#     th1 = Process(target=countdown, args=[1_000_000_000])
#     th2 = Process(target=countdown, args=[1_000_000_000])
#
#     th1.start()
#     th2.start()
#
#     print(current_process())
#
#     th1.join()
#     th2.join()
#
#     print(f'Execution time: {time() - start}')


# from multiprocessing import Process, Pool
# from time import time
#
# import requests
#
# urls = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://meta.wikimedia.org/wiki/Wikipedia/uk',
#     'https://itc.ua/tag/wikipedia/'
# ] * 1000
#
#
# def foo(url):
#     response = requests.get(url)
#
#
# if __name__ == '__main__':
#     start = time()
#
#     with Pool(60) as p:
#         print(p.map(foo, urls))
#
#     print(f'Execution time: {time() - start}')



from multiprocessing import Process, Queue
from time import time, sleep

import requests

urls = [
    'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
    'https://meta.wikimedia.org/wiki/Wikipedia/uk',
    'https://itc.ua/tag/wikipedia/'
] * 100


def foo(queue):
    while True:
        url = queue.get()
        print(f'foo: {url}')

        if url is None:
            break

        requests.get(url)


if __name__ == '__main__':
    start = time()

    que = Queue()

    pr = Process(target=foo, args=[que])
    pr2 = Process(target=foo, args=[que])
    pr.start()
    pr2.start()

    for url in urls:
        print(f'put to que')
        que.put(url)

    que.put(None)
    que.put(None)

    print(f'Execution time: {time() - start}')

