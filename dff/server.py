from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

import codecs
import pickle
from annotators.nlu_client import NluClient

from scenario.main import actor
from df_engine.core import Actor, Context
from annotators.main import annotate

class Message(BaseModel):
    text: str
    ctx: Optional[str] = None


app = FastAPI(on_startup=[NluClient.on_start], on_shutdown=[NluClient.on_close])

@app.post('/psy-chat/')
async def handle_utter(msg: Message):
    ctx = ctx_decode(msg.ctx) 
    ctx.add_request(msg.text)

    ctx = await annotate(ctx)
    ctx = actor(ctx)
    
    return Message(
        text=ctx.last_response, 
        ctx=ctx_encode(ctx))

@app.get('/healthcheck')
def healthcheck():
    return 'I am alive'


def ctx_encode(ctx: Context) -> str:
    return codecs.encode(pickle.dumps(ctx), 'base64').decode()

def ctx_decode(ctx: str) -> Context:
    if ctx == None:
        return Context()
    return pickle.loads(codecs.decode(ctx.encode(), 'base64'))