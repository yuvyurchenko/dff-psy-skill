from df_engine.core import Actor, Context

from model.main import DUMMY_ANNOTATION, Annotation, Intent, Subtopic


def greetings(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    return annotation(ctx).intent.type == Intent.GREET

def exp_info(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    intent = annotation(ctx).intent
    return intent.type == Intent.EXPERIMENT_TALK \
        and intent.data.subtopic_id == Subtopic.INFO \
        and intent.data.topic_id is not None

def exp_subtopic(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    intent = annotation(ctx).intent
    return intent.type == Intent.EXPERIMENT_TALK \
        and intent.data.subtopic_id != Subtopic.INFO

def term_explain(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    return annotation(ctx).intent.type == Intent.TERM_EXPLAIN

def annotation(ctx: Context) -> Annotation:
    return ctx.misc.get('annotation', DUMMY_ANNOTATION)
