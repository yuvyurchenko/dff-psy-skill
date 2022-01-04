import yaml

from model.main import Lang, Subtopic
from scenario.condition import term_explain

with open('datastore/data_en.yaml', 'r', encoding='utf-8') as f:
    data_en = yaml.safe_load(f)

def get_experiment(lang: Lang, id: str) -> dict:
    return get_data(lang)['experiments'][id]

def get_experiment_details(lang: Lang, id: str, subtopic: Subtopic):
    all_details = get_experiment(lang, id)
    if subtopic == Subtopic.INFO:
        return {
            'title': all_details['title'],
            'year': all_details['year'],
            'author': all_details['author']
        }
    elif subtopic == Subtopic.PREMISE:
        return all_details['premise']
    elif subtopic == Subtopic.CONDUCT:
        return all_details['conduct']
    elif subtopic == Subtopic.OUTCOME:
        return all_details['outcome']
    else:
        raise ValueError(f'Unknown subtopic: {subtopic}')

def get_term(lang: Lang, term: str) -> str:
    terms = get_data(lang)['terms']
    if term in terms:
        return terms[term]
    else:
        return None

def get_data(lang: Lang):
    if lang == Lang.EN:
        return data_en
    elif lang == Lang.RUS:
        raise ValueError('Unsupported language yet')
    else:
        raise ValueError(f'Unsupported language: {lang}')