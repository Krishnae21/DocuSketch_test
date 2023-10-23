#!/bin/bash

THRESHOLD=5
API_ENDPOINT=""
API_KEY=""

MEMORY_USAGE=$(free | awk 'NR==2{printf "%.2f\n", $3*100/$2}')

if awk -v memory_usage="$MEMORY_USAGE" -v threshold="$THRESHOLD" 'BEGIN { exit (memory_usage > threshold) ? 0 : 1 }'; then
    curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $API_KEY"  -d '{"memory_usage": '$MEMORY_USAGE'}' $API_ENDPOINT >/dev/null 2>&1
    echo "There's not much memory left. Alarm send."
    else
      echo "Memory is ok."
fi;