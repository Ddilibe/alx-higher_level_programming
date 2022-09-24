#!/usr/bin/python3
"""
    Script tha retrieves the commits of a particular
"""

if __name__ == "__main__":
    import sys
    import requests

    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1], sys.argv[2])
    req = requests.get(url)
    for keys in req.json():
        print(req.json()[0]['sha'])
