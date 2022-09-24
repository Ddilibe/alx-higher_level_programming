#!/usr/bin/python3
"""
    Scrip that takes in a letter and sends a post request to 
    https://0.0.0.0:5000/search_user with the letter as a 
    parameter
"""

if __name__ == "__main__":
    import requests
    import sys

    load = {}
    if len(sys.argv) > 1:
        load['q'] = sys.argv[1]
    else:
        load['q'] = ""
    req = requests.post("http://0.0.0.0:5000/search_user", data=load)
    try:
        print(req.json())
        john = req.json()
        if john:
            print("[{}] {}".format(john['id'], john['name']))
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
