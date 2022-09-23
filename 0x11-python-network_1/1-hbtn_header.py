#!/usr/bin/python3
"""
    Script that takes in a url, sends the request to the url and
    displays the value of the X-Request-Id variable found in the
    header of the response
"""

if __name__ == '__main__':
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        id = response.getheader('X-Request-Id')
        print(id)
