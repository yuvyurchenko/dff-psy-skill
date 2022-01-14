from model.main import Annotation, ExperimentData, IntentDetails, Lang, Intent, Subtopic, TermData
from typing import Optional
from aiohttp import ClientSession

paths_per_lang = {
    Lang.EN: 'http://rasa-nlu-en:5005/model/parse',
    Lang.RUS: 'http://rasa-nlu-ru:5005/model/parse'
}

intent_inventory = {
    "greet": Intent.GREET,
    "question": Intent.TERM_EXPLAIN,
    "experiment_init": Intent.EXPERIMENT_TALK,
    "experiment_premise": Intent.EXPERIMENT_TALK,
    "experiment_conduct": Intent.EXPERIMENT_TALK,
    "experiment_outcome": Intent.EXPERIMENT_TALK
}

exp_subtopic_inventory = {
    "experiment_init": Subtopic.INFO,
    "experiment_premise": Subtopic.PREMISE,
    "experiment_conduct": Subtopic.CONDUCT,
    "experiment_outcome": Subtopic.OUTCOME
}

class NluClient:
    _session: Optional[ClientSession] = None

    @classmethod
    async def understand_utterance(cls, lang: Lang, utter: str, prev_topic_id: str):
        if cls._session is None:
            raise ConnectionError('HTTP Session is not initialized')

        async with cls._session.post(paths_per_lang[lang], json={"text": utter}) as resp:
            data = await resp.json()

            rasa_intent_id = data['intent']['name']

            intent_type = intent_inventory.get(rasa_intent_id, Intent.OTHER)
            
            if intent_type == Intent.TERM_EXPLAIN:
                entities = data['entities']
                if len(entities) == 0:
                    term = None
                else:
                    term = entities[0]['value']

                intent_data = TermData(
                    term=term, 
                    topic_id=prev_topic_id)

            elif intent_type == Intent.EXPERIMENT_TALK:
                subtopic = exp_subtopic_inventory[rasa_intent_id]
                if subtopic == Subtopic.INFO:
                    topic_id = data['response_selector']['default']['response']['utter_action'][22:]
                else:
                    topic_id = prev_topic_id

                intent_data = ExperimentData(
                    topic_id=topic_id, 
                    subtopic_id=subtopic)

            else:
                intent_data = None
            
            return Annotation(
                lang=lang, 
                intent=IntentDetails(
                    type=intent_type, 
                    data=intent_data))
    
    @classmethod
    async def on_start(cls):
        cls._session = ClientSession()    

    @classmethod
    async def on_close(cls):
        await cls._session.close()
        cls._session = None
