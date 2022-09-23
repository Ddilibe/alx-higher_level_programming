#!/usr/bin/python3
"""
    Script tha retrieves the commits of a particular
"""

if __name__ == "__main__":
    import sys
    import requests
    import json

    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1], sys.argv[2])
    req = requests.get(url)
    for keys in req.json():
        with open("jam", 'w') as k:
            for i in req.json():
               json.dump(k, json.load(i))
