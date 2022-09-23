#!/usr/bin/python3
"""
    Script that detched https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests
    req = requests.get("https://alx-intranet.hbtn.io/status")
    details = {}
    details['type'], details['content'], = type(req.text), req.text
    print("Body response:")
    for key, value in details.items():
        print("\t- {}: {}".format(key, value))
