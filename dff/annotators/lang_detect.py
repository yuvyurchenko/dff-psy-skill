import re
from model.main import Lang

ru_pattern = re.compile('[а-яА-я]')

def detect_lang(txt: str) -> Lang:
    if ru_pattern.search(txt):
        return Lang.RUS
    else:
        return Lang.EN