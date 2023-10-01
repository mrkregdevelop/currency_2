import requests
from sanic import Sanic
from sanic.response import text
import httpx

app = Sanic("MyHelloWorldApp")


@app.get("/")
async def hello_world(request):
    async with httpx.AsyncClient() as client:
        response = await client.get('https://itc.ua/tag/wikipedia/')

    return text(str(response.status_code))
