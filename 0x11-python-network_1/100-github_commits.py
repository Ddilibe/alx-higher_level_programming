#!/usr/bin/python3
"""
    Script tha retrieves the commits of a particular
"""

if __name__ == "__main__":
    import sys
    import requests
    import json

    url = "https://api.github.com/repos/{}/{}/commits".\
        format(sys.argv[1], sys.argv[2])
    req = requests.get(url)
    jam = req.json()
    jam = jam[::-1]
    for k in range(10):
        sha = jam[k].get("sha")
        if "commit" in jam[k]:
            if "author" in jam[k].get("commit"):
                if "name" in jam[k].get("commit").get("author"):
                    name = jam[k].get("commit").get("author").get("name")
                else:
                    name = ""
            else:
                name = ""
        else:
            name = ""
        print("{}: {}".format(sha, name))
