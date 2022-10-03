#!/bin/bash
# Script that requests a url and displays the status code of
# the response
curl -o /dev/null -s -w "%{http_code}\n" "$1"
