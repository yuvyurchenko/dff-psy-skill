from enum import Enum, auto
from df_engine.core import Context

from model.main import Intent, Lang, Subtopic

def annotate(ctx: Context):
    if 'Explain ' in ctx.last_request:
        ctx.misc['lang'] = Lang.EN
        ctx.misc['intent'] = {
            'type': Intent.TERM_EXPLAIN,
            'data': {
                'term': ctx.last_request[len('Explain '):].lower(),
                'topic_id': topic_id(ctx)
            }
        }
    elif 'What was an experiment about the prison?' == ctx.last_request:
        ctx.misc['lang'] = Lang.EN
        ctx.misc['intent'] = {
            'type': Intent.EXPERIMENT_TALK,
            'data': {
                'topic_id': 'exp_2',
                'subtopic_id': Subtopic.INFO
            }
        }
    elif 'Give me the premise' == ctx.last_request:
        ctx.misc['lang'] = Lang.EN
        ctx.misc['intent'] = {
            'type': Intent.EXPERIMENT_TALK,
            'data': {
                'topic_id': topic_id(ctx),
                'subtopic_id': Subtopic.PREMISE
            }
        }
    elif 'How was it conducted?' == ctx.last_request:
        ctx.misc['lang'] = Lang.EN
        ctx.misc['intent'] = {
            'type': Intent.EXPERIMENT_TALK,
            'data': {
                'topic_id': topic_id(ctx),
                'subtopic_id': Subtopic.CONDUCT
            }
        }
    elif 'What was the outcome?' == ctx.last_request:
        ctx.misc['lang'] = Lang.EN
        ctx.misc['intent'] = {
            'type': Intent.EXPERIMENT_TALK,
            'data': {
                'topic_id': topic_id(ctx),
                'subtopic_id': Subtopic.OUTCOME
            }
        }
    else:
        ctx.misc['lang'] = Lang.EN
        ctx.misc['intent'] = {
            'type': Intent.OTHER,
            'data': {} 
        }

    return ctx


def topic_id(ctx: Context):
    if 'topic_id' in ctx.misc['intent']['data']:
        return ctx.misc['intent']['data']['topic_id']
    else:
        return ''