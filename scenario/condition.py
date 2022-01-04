from logging import INFO
from df_engine.core import Actor, Context
import df_engine.conditions as cnd

from annotators.main import Intent, Subtopic


def greetings(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    return cnd.exact_match('Hi')(ctx, actor, *args, **kwargs)

def exp_info(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    if 'intent' not in ctx.misc:
        return False

    return ctx.misc['intent']['type'] == Intent.EXPERIMENT_TALK \
        and ctx.misc['intent']['data']['subtopic_id'] == Subtopic.INFO

def exp_premise(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    if 'intent' not in ctx.misc:
        return False
    
    return ctx.misc['intent']['type'] == Intent.EXPERIMENT_TALK \
        and ctx.misc['intent']['data']['subtopic_id'] == Subtopic.PREMISE

def exp_conduct(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    if 'intent' not in ctx.misc:
        return False
    
    return ctx.misc['intent']['type'] == Intent.EXPERIMENT_TALK \
        and ctx.misc['intent']['data']['subtopic_id'] == Subtopic.CONDUCT

def exp_outcome(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    if 'intent' not in ctx.misc:
        return False
    
    return ctx.misc['intent']['type'] == Intent.EXPERIMENT_TALK \
        and ctx.misc['intent']['data']['subtopic_id'] == Subtopic.OUTCOME

def term_explain(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    if 'intent' not in ctx.misc:
        return False

    return ctx.misc['intent']['type'] == Intent.TERM_EXPLAIN

