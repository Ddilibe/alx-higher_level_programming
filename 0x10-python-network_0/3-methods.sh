#!/bin/bash
# Script that takes in a url and displays all the HTTP methods the server will accept
curl -Is "$1" | grep "Allow:" | cut -d " " -f 2
