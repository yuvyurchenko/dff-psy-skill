import logging
import logging.config
from pathlib import Path
import yaml

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

import codecs
import pickle
from annotators.nlu_client import NluClient

from scenario.main import actor
from df_engine.core import Actor, Context
from annotators.main import annotate

Path('logs/').mkdir(exist_ok=True)

with open('logconf.yaml', 'r') as f:
    cfg = yaml.safe_load(f.read())
    logging.config.dictConfig(cfg)

logger = logging.getLogger('serverLogger')

class Message(BaseModel):
    text: str
    ctx: Optional[str] = None

app = FastAPI(on_startup=[NluClient.on_start], on_shutdown=[NluClient.on_close])

@app.post('/psy-chat/')
async def handle_utter(msg: Message):
    logger.debug('request - handle_utter with msg: %s', msg)
    
    ctx = ctx_decode(msg.ctx) 
    ctx.add_request(msg.text)

    try:
        logger.debug('ctx - before processing: %s', ctx)

        ctx = await annotate(ctx)
        ctx = actor(ctx)

        logger.debug('ctx - after processing: %s', ctx)
    except Exception:
        logging.exception('processing failed')
        
        response = Message(
            text='It hurts!!!', 
            ctx=None)
    else:
        response = Message(
            text=ctx.last_response, 
            ctx=ctx_encode(ctx))

    logger.debug('response - handle_utter: %s', response)
    
    return response

@app.get('/healthcheck')
def healthcheck():
    logger.debug('request - healtcheck')
    return 'I am alive'


def ctx_encode(ctx: Context) -> str:
    return codecs.encode(pickle.dumps(ctx), 'base64').decode()

def ctx_decode(ctx: str) -> Context:
    if ctx == None:
        return Context()
    return pickle.loads(codecs.decode(ctx.encode(), 'base64'))