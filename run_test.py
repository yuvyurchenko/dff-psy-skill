import random
from datastore.main import get_data
from model.main import Lang

from scenario.main import actor
import run_interactive

random.seed(314)

# testing
testing_dialog = [
    ("Hi", "Hi, how are you? I can tell you about some classical psychological experiments or explain a few psychological terms."),
    ("Explain experiment", get_data(Lang.EN)['terms']['experiment']),
    ("Explain bla-bloo-blop", "No idea what are you talking about."),
    ("What was an experiment about the prison?", "The name of the experient is Stanford Prison Experiment. It was conducted in year 1971 by Philip Zimbardo"),
    ("Give me the premise", get_data(Lang.EN)['experiments']['exp_2']['premise']),
    ("What was the outcome?", get_data(Lang.EN)['experiments']['exp_2']['outcome']),
    ("Explain conformity", get_data(Lang.EN)['terms']['conformity']), # change flow
    ("How was it conducted?", get_data(Lang.EN)['experiments']['exp_2']['conduct']) # go back to the previous topic
]


def run_test():
    ctx = {}
    for in_request, true_out_response in testing_dialog:
        _, ctx = run_interactive.turn_handler(in_request, ctx, actor, true_out_response=true_out_response)
    print("test passed")


if __name__ == "__main__":
    run_test()
