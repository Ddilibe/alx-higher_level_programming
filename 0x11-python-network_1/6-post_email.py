#!/usr/bin/python3
"""
    Script that takes in a url and an email address, sends apost
    request with the passed url with the email as a parameter and
    finally displays the body of the response
"""

if __name__ == "__main__":
    import requests
    import sys

    data = {"email": sys.argv[2]}
    got = requests.post(sys.argv[1], data=data)
    print("{}".format(got.text))
