#!/bin/bash
# send request > URL with curl + displays: size of the body of the response
curl -s "$1" | wc -c
