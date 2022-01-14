#!/bin/bash

set -e

cmd="$@"

until curl http://rasa-nlu-en:5005/; do
	echo "waiting to load en nlu model..."
	sleep 15
done

until curl http://rasa-nlu-ru:5005/; do
	echo "waiting to load ru nlu model..."
	sleep 15
done

echo "ready"

exec $cmd