from enum import Enum, auto

class Intent(Enum):
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