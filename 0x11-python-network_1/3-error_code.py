#!/usr/bin/python3
"""
    Script that takes in a url, sends a request to the url and displays
    the body of the response decoded in utf-8
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()
            print(content.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
