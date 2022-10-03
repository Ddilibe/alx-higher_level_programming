#!/usr/bin/python3
"""
    Script that takes in a url, sends a request to the url and displays
    the value of the variable X-Request-Id in the response header
"""

if __name__ == "__main__":
    import requests
    import sys
    req = requests.get(sys.argv[1])
    print(req.headers['X-Request-Id'])
