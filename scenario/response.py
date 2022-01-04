
from df_engine.core.actor import Actor
from df_engine.core.context import Context

from datastore.main import get_experiment_details, get_term
from model.main import Lang, Subtopic
from templates.main import fallback, generate_info_response, greatings, no_term_explanation, validation

def greetings_response(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    if 'lang' not in ctx.misc:
        return validation()

    lang = ctx.misc['lang']
    return greatings(lang)

def fallback_response(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    if 'lang' not in ctx.misc:
        return validation()

    lang = ctx.misc['lang']
    return fallback(lang)

def info_response(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    if 'lang' not in ctx.misc:
        return validation()

    lang = ctx.misc['lang']
    topic_id = ctx.misc['intent']['data']['topic_id']
    info = get_experiment_details(lang, topic_id, Subtopic.INFO)
    return generate_info_response(lang, info) 

def premise_response(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    if 'lang' not in ctx.misc:
        return validation()

    lang = ctx.misc['lang']
    topic_id = ctx.misc['intent']['data']['topic_id']
    return get_experiment_details(lang, topic_id, Subtopic.PREMISE)

def conduct_response(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    if 'lang' not in ctx.misc:
        return validation()

    lang = ctx.misc['lang']
    topic_id = ctx.misc['intent']['data']['topic_id']
    return get_experiment_details(lang, topic_id, Subtopic.CONDUCT)

def outcome_response(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    if 'lang' not in ctx.misc:
        return validation()

    lang = ctx.misc['lang']
    topic_id = ctx.misc['intent']['data']['topic_id']
    return get_experiment_details(lang, topic_id, Subtopic.OUTCOME)

def term_response(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    if 'lang' not in ctx.misc:
        return validation()

    lang = ctx.misc['lang']
    term = ctx.misc['intent']['data']['term']
    explanation = get_term(lang, term)
    if explanation is None:
        return no_term_explanation(lang)
    else:
        return explanation
