#!/bin/bash
# Script that sends a Json POst request to a URL passed as
# the first argument an d@$2" -H "Content-Type: application/json"e
curl -s "$1" -X POST -d "$2"
