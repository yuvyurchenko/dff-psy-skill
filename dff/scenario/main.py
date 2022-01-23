from df_engine.core import Actor
from df_engine.core.keywords import LOCAL, RESPONSE, TRANSITIONS
import df_engine.conditions as cnd
import df_engine.labels as lbl

import scenario.condition as loc_cnd
import scenario.response as loc_resp

plot = {
    "global_flow": {
        "start": {
            RESPONSE: "",
            TRANSITIONS: {
                "greetings_node": loc_cnd.greetings
            },
        },
        "greetings_node": {
            RESPONSE: loc_resp.greetings_response,
            TRANSITIONS: {
                ("experiment_flow", "info"): loc_cnd.exp_info,
                ("terms_flow", "explain"): loc_cnd.term_explain
            }
        },
        "fallback": {
            RESPONSE: loc_resp.fallback_response,
            TRANSITIONS: {
                ("experiment_flow", "info"): loc_cnd.exp_info,
                ("terms_flow", "explain"): loc_cnd.term_explain
            }
        },
    },
    "experiment_flow": {
        "info": {
            RESPONSE: loc_resp.info_response,
            TRANSITIONS: {
                "info": loc_cnd.exp_info,
                "subtopic": loc_cnd.exp_subtopic,
                ("terms_flow", "explain"): loc_cnd.term_explain
            }
        },
        "subtopic": {
            RESPONSE: loc_resp.subtopic_response,
            TRANSITIONS: {
                "info": loc_cnd.exp_info,
                "subtopic": loc_cnd.exp_subtopic,
                ("terms_flow", "explain"): loc_cnd.term_explain
            }
        }
    },
    "terms_flow": {
        "explain": {
            RESPONSE: loc_resp.term_response,
            TRANSITIONS: {
                ("experiment_flow", "info"): loc_cnd.exp_info,
                ("experiment_flow", "subtopic"): loc_cnd.exp_subtopic,
                "explain": loc_cnd.term_explain
            }
        }
    }
}

actor = Actor(plot, start_label=("global_flow", "start"), fallback_label=("global_flow", "fallback"))
