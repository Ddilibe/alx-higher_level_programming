#!/usr/bin/env bash
# Script that displays the size of the body of the response
curl -Is "$1" | grep "Content-Length:" | cut -d " " -f 2
