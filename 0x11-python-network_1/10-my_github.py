#!/usr/bin/python3
"""
    Script that takes your github cerdentials (username and
    password and uses the github api to display your id
"""

if __name__ == "__main__":
    import sys
    import requests

    basic = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get('https://api.github.com/user', auth=basic)
    test = req.text
    print(req)
