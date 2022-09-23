#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me that causes
# the server to respond with a message containing "You got me!"
curl -sLi 0.0.0.0:5000/catch_me -X PUT -F "user_id=98"
