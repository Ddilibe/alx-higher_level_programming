#!/bin/bash
# Script that takes a url argument and displays the body of the response
curl -X "$1" -H "X-School-User-Id: 98"
