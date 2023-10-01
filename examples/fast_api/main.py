import hashlib
import hmac
from os import environ

from fastapi import FastAPI, Request
from pydantic import BaseModel

import databases

from models import zoom_webhook_event_table


DB_USER = environ.get("DB_USER", "user")
DB_PASSWORD = environ.get("DB_PASS", "password")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_NAME = environ.get("DB_NAME", "localhost")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+aiopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)

database = databases.Database(SQLALCHEMY_DATABASE_URL)


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


class ZoomWebhookEvent(BaseModel):
    event: str
    payload: dict
    event_ts: int


@app.post('/zoom/webhook/')
async def zoom_webhook(webhook_event: ZoomWebhookEvent):
    if webhook_event.event == 'endpoint.url_validation':
        message = hmac.new(bytes('1h1VdBuNTxSpsmOyiPiSUw', 'latin-1'),
                           msg=bytes(webhook_event.payload['plainToken'], 'latin-1'),
                           digestmod=hashlib.sha256).hexdigest()
        return {
            'plainToken': webhook_event.payload['plainToken'],
            'encryptedToken': message
        }

    query = zoom_webhook_event_table.insert().values(**webhook_event.dict())
    item_id = await database.execute(query)

    return {}

'''
PoC - Proof of Concept
'''
