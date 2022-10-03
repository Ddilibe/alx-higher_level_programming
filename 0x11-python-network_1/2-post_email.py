#!/usr/bin/python3
"""
    Script that takes in a url and an email, sends a POST request to the
    passed url with the email as the parameter and displays the body of
    the response decoded in utf-8
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    values = {'email': sys.argv[2]}
    u = sys.argv[1]
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(u, data)
    with urllib.request.urlopen(req) as response:
        email = response.read()
        print("{}".format(email.decode('utf-8')))
