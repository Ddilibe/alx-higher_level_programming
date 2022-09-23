#!/bin/bash
# Script that sends a Json POst request to a URL passed as
# the first argument an displays the body of the response
curl -s "$1" -X POST -d "$2"
