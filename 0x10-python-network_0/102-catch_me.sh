#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me that causes
# the server to respond with a message containing "You got me!"
curl -sL 0.0.0.0:5000/catch_me_2 -X PUT -F "user_id=98"
