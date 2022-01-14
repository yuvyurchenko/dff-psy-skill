from df_engine.core import Context

from annotators.lang_detect import detect_lang
from annotators.nlu_client import NluClient

async def annotate(ctx: Context):
    lang = detect_lang(ctx.last_request)
    prev_annotation = ctx.misc.get('annotation', None)
    if prev_annotation is not None and prev_annotation.intent.data is not None:
        prev_topic_id = prev_annotation.intent.data.topic_id
    else:
        prev_topic_id = None

    ctx.misc['annotation'] = await NluClient.understand_utterance(lang, ctx.last_request, prev_topic_id)
    return ctx
