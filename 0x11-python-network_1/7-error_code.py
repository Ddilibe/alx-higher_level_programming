#!/usr/bin/python3
"""
    Script thst tskes in a url, sends a request to the url 
    and displays the body of the response
"""

if __name__ == "__main__":
    import requests
    import sys

    try:
        req = requests.get(sys.argv[1])
        if req.status_code == requests.codes.ok:
            print(req.text)
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(req.status_code))
