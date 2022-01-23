import random
import yaml
from run_interactive import ask, wait_init

random.seed(314)

with open('dff/datastore/data_en.yaml', 'r', encoding='utf-8') as f:
    data_en = yaml.safe_load(f)

with open('dff/datastore/data_ru.yaml', 'r', encoding='utf-8') as f:
    data_ru = yaml.safe_load(f)

testing_dialog = [
    ("Hi", "Hi, how are you? I can tell you about some classical psychological experiments or explain a few psychological terms."),
    ("Explain experiment", data_en['terms']['experiment']),
    ("Explain bla-bloo-blop", "No idea what are you talking about."),
    ("What was an experiment about the prison?", "The name of the experient is Stanford Prison Experiment. It was conducted in year 1971 by Philip Zimbardo"),
    ("Give me the premise", data_en['experiments']['exp_2']['premise']),
    ("What was the outcome?", data_en['experiments']['exp_2']['outcome']),
    ("Explain conformity", data_en['terms']['conformity']), # change flow
    ("How was it conducted?", data_en['experiments']['exp_2']['conduct']), # go back to the previous topic
    ("hfgdhhdhdhhdhdh hhdhhfsfhdskjfhkd hsdjkfhdskfksdfds", "Sorry, didn't get you =("), # fallback
    ("Знаешь ли какие-то эксперименты исследующие конформизим?", "Название эксперимента: Исследование конформизма Аша. Дата проведения: 1951. Автор: Соломон Аш"), # transparently switch the language
    ("Что такое конформизм?", data_ru['terms']['конформизм']), # change flow
    ("Что такое мурмур?", "Друг, ты о чём?"), # asking about unknown term handling
    ("В чём была исходная идея?", data_ru['experiments']['exp_3']['premise']),
    ("Как они это сделали?", data_ru['experiments']['exp_3']['conduct']),
    ("Какие были сделаны выводы?", data_ru['experiments']['exp_3']['outcome'])
]


if __name__ == "__main__":
    wait_init()
    ctx = None
    for text, true_text_response in testing_dialog:
        text_response, ctx = ask(text, ctx)
        if true_text_response is not None and true_text_response != text_response:
            raise Exception(f"{text=} -> true_out_response != out_response: {true_text_response} != {text_response}")
    print("test passed")