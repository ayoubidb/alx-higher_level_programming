#!/bin/bash
# Send a POST request > to the passed URL using curl + display: the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
