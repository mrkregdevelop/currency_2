# from time import sleep, time
#
#
# def foo():
#     print('1')
#     sleep(1)
#     print('2')
#
#
# start = time()
#
# for i in range(3):
#     foo()
#
# print(f'Execution time: {time() - start}')
#
# import asyncio
# from time import time
#
#
# async def foo_async():
#     print('1')
#     await asyncio.sleep(1)
#     print('2')
#
#
# async def main():
#     await asyncio.gather(foo_async(), foo_async(), foo_async())
#
#
# start = time()
#
# asyncio.run(main())  # event loop
#
# print(f'Execution time: {time() - start}')


# def foo_generator():
#     for i in range(3):
#         print('1')
#         yield i
#
#
# for j in foo_generator():
#     print('2')

# from time import time
#
# import requests
#
# urls = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://meta.wikimedia.org/wiki/Wikipedia/uk',
#     'https://itc.ua/tag/wikipedia/'
# ] * 50
#
# start = time()
#
#
# def sync_get_url(url):
#     response = requests.get(url)
#     print(response.status_code)
#
#
# for url in urls:
#     sync_get_url(url)
#
#
# print(f'Execution time: {time() - start}')

# import requests
# from time import time
# from threading import Thread
#
# urls = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://meta.wikimedia.org/wiki/Wikipedia/uk',
#     'https://itc.ua/tag/wikipedia/'
# ] * 50
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
#
# from time import time
# import asyncio
# import httpx
#
# urls = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://meta.wikimedia.org/wiki/Wikipedia/uk',
#     'https://itc.ua/tag/wikipedia/'
# ] * 50
#
#
# async def foo_async(url):
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)
#     print(response.status_code)
#
#
# async def main():
#     tasks = []
#     for url in urls:
#         tasks.append(foo_async(url))
#
#     await asyncio.gather(*tasks)
#
# start = time()
#
# asyncio.run(main())  # event loop
#
# print(f'Execution time: {time() - start}')


# from time import time
# import asyncio
# import httpx
#
#
# async def foo_async(url: str) -> None:
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, timeout=30.0)
#     print(response.status_code)
#
#
# async def main():
#     tasks = []
#     for i in range(30):
#         tasks.append(foo_async('http://127.0.0.1:8000/'))
#
#     await asyncio.gather(*tasks)
#
# start = time()
#
# asyncio.run(main())  # event loop
#
# print(f'Execution time: {time() - start}')

'''
ASGI - WSGI
'''