from model.main import Lang

def info_response_template_ru(info: dict) -> str:
    return f"Название эксперимента: {info['title']}. Дата проведения: {info['year']}. Автор: {info['author']}"

def info_response_template_en(info: dict) -> str:
    return f"The name of the experient is {info['title']}. It was conducted in year {info['year']} by {info['author']}"

info_response_templates = {
    Lang.EN: info_response_template_en,
    Lang.RUS: info_response_template_ru  
}

no_term_explanation_templates = {
    Lang.EN: 'No idea what are you talking about.',
    Lang.RUS: 'Друг, ты о чём?'
}

greatings_templates = {
    Lang.EN: "Hi, how are you? I can tell you about some classical psychological experiments or explain a few psychological terms.",
    Lang.RUS: "Привет! Я могу рассказать о некоторых классических экспериментах в психологии или объяснить парочку психологических терминов."
}

fallback_templates = {
    Lang.EN: "Sorry, didn't get you =(",
    Lang.RUS: "Извини, не понял тебя =("
}

def generate_info_response(lang: Lang, info: dict) -> str:
    return info_response_templates[lang](info)

def no_term_explanation(lang: Lang):
    return no_term_explanation_templates[lang]

def greatings(lang: Lang):
    return greatings_templates[lang]

def fallback(lang: Lang):
    return fallback_templates[lang]

def validation():
    return 'I am ok!'