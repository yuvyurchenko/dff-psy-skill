
from df_engine.core.actor import Actor
from df_engine.core.context import Context

from datastore.main import get_experiment_details, get_term
from model.main import Annotation, Lang, Subtopic
from templates.main import fallback, generate_info_response, greatings, no_term_explanation, validation

def greetings_response(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    if no_annotation(ctx):
        return validation()
    return greatings(annotation(ctx).lang)

def fallback_response(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    if no_annotation(ctx):
        return validation()
    return fallback(annotation(ctx).lang)

def info_response(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    if no_annotation(ctx):
        return validation()
    lang = annotation(ctx).lang
    topic_id = annotation(ctx).intent.data.topic_id
    info = get_experiment_details(lang, topic_id, Subtopic.INFO)
    return generate_info_response(lang, info) 

def subtopic_response(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    if no_annotation(ctx):
        return validation()
    lang = annotation(ctx).lang
    topic_id = annotation(ctx).intent.data.topic_id
    subtopic_id = annotation(ctx).intent.data.subtopic_id
    return get_experiment_details(lang, topic_id, subtopic_id)

def term_response(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    if no_annotation(ctx):
        return validation()
    lang = annotation(ctx).lang
    term = annotation(ctx).intent.data.term
    explanation = get_term(lang, term)
    if explanation is None:
        return no_term_explanation(lang)
    else:
        return explanation

def no_annotation(ctx: Context) -> bool:
    return 'annotation' not in ctx.misc

def annotation(ctx: Context) -> Annotation:
    return ctx.misc['annotation']