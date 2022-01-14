from enum import Enum, auto
from dataclasses import dataclass
from typing import Any

class Intent(Enum):
    GREET = auto()
    TERM_EXPLAIN = auto()
    EXPERIMENT_TALK = auto()
    OTHER = auto()

class Subtopic(Enum):
    INFO = auto()
    PREMISE = auto()
    CONDUCT = auto()
    OUTCOME = auto()

class Lang(Enum):
    EN = auto()
    RUS = auto()

@dataclass
class TermData:
    term: str
    topic_id: str

@dataclass
class ExperimentData:
    topic_id: str
    subtopic_id: Subtopic

@dataclass
class IntentDetails:
    type: Intent
    data: Any

@dataclass
class Annotation:
    lang: Lang
    intent: IntentDetails

DUMMY_ANNOTATION = Annotation(lang=Lang.EN, intent=IntentDetails(type=Intent.OTHER, data=None))