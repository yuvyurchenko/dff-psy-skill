# DFF Psychological Skill

## Description

### Overview
The bot can chat about some classical psychological experiments and explain specific terms from them.
It can speak English and Russian languages.

### Components
The bot consists of 3 services:
- dff servce:
    - rest-api to communicate with the bot
    - DFF framework to orchestrate dialog flows
    - language classification (naive character-driven approach)
    - datastore: simple file-db storing data for responses in yaml-files
    - nlu-client to communicate with RASA NLU services
- rasa-nlu-en service:
    - RASA NLU module: intent detection and entity extraction for English language
- rasa-nlu-ru service
    - RASA NLU module: intent detection and entity extraction for Russian language

### Configuration

The following article has been used as a source of knowladge for the bot (for Russian language the same article has been auto-transalated with minor manual corrections):

https://online.king.edu/news/psychology-experiments/

However, the knowladge base can be extended via configuration if the new experiment description fits into the same format.

#### Steps
1. Update datastore file
2. Update RASA DSL file to understand questions related to the new data

#### File locations per language
- English
    - datastore file: /dff/datastore/data_en.yaml
    - RASA DSL file: /nlu_services/nlu_en/nlu.yaml
- Russian
    - datastore file: /dff/datastore/data_ru.yaml
    - RASA DSL file: /nlu_services/nlu_ru/nlu.yaml

## Quickstart

```bash
pip install -r requirements.txt
docker-compose up -d
```
Run interactive mode
```bash
python run_interactive.py
```
Run tests
```bash
python run_test.py
```

## Resources
* Execution time: 0.15 sec avg
* Starting time: 2:24 min
* RAM: 1.63 GB
