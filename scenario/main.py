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
            RESPONSE: loc_resp.fallback_response
        },
    },
    "experiment_flow": {
        "info": {
            RESPONSE: loc_resp.info_response,
            TRANSITIONS: {
                "info": loc_cnd.exp_info,
                "premise": loc_cnd.exp_premise,
                "conduct": loc_cnd.exp_conduct,
                "outcome": loc_cnd.exp_outcome,
                ("terms_flow", "explain"): loc_cnd.term_explain
            }
        },
        "premise": {
            RESPONSE: loc_resp.premise_response,
            TRANSITIONS: {
                "info": loc_cnd.exp_info,
                "premise": loc_cnd.exp_premise,
                "conduct": loc_cnd.exp_conduct,
                "outcome": loc_cnd.exp_outcome,
                ("terms_flow", "explain"): loc_cnd.term_explain
            }
        },
        "conduct": {
            RESPONSE: loc_resp.conduct_response,
            TRANSITIONS: {
                "info": loc_cnd.exp_info,
                "premise": loc_cnd.exp_premise,
                "conduct": loc_cnd.exp_conduct,
                "outcome": loc_cnd.exp_outcome,
                ("terms_flow", "explain"): loc_cnd.term_explain
            }
        },
        "outcome": {
            RESPONSE: loc_resp.outcome_response,
            TRANSITIONS: {
                "info": loc_cnd.exp_info,
                "premise": loc_cnd.exp_premise,
                "conduct": loc_cnd.exp_conduct,
                "outcome": loc_cnd.exp_outcome,
                ("terms_flow", "explain"): loc_cnd.term_explain
            }
        }
    },
    "terms_flow": {
        "explain": {
            RESPONSE: loc_resp.term_response,
            TRANSITIONS: {
                ("experiment_flow", "info"): loc_cnd.exp_info,
                ("experiment_flow", "premise"): loc_cnd.exp_premise,
                ("experiment_flow", "conduct"): loc_cnd.exp_conduct,
                ("experiment_flow", "outcome"): loc_cnd.exp_outcome,
                "explain": loc_cnd.term_explain
            }
        }
    }
}

actor = Actor(plot, start_label=("global_flow", "start"), fallback_label=("global_flow", "fallback"))
