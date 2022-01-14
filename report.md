# Report

## Week 1

### TODO
- serch for an experiment by different descriptions
- slot filling
- ru lang support

### WIP
- existing nlp libs chech for intent detection and slot filling

### Done
- flow configuration
- basic impl for annotation & condition parts
- datastore

## Week 2

### TODO
- support more scenarios in both EN and RU NLU models
- check confidence of NLU models
- think about more smart language classification. not clear what is the most optimal approach with short messages in chat
- translate data in datastore to russian
- logging

### WIP
- NLU model and datastore updates

### Done
- I have chosen RASA NLU, created basic model to support previously written test scenario
- solution is containerized: each language NLU model is deployed as a separate container + container with dff orchestrating incomming messages processing; run_interactive/run_test have been changed to work via http 

## Week 3
TBD

## Week 4
TBD