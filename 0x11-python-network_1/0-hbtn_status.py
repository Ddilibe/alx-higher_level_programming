#!/usr/bin/python3
"""
    A python script that fetches 'https://alx-intranet.hbtn.io/status'
"""

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    details = {}
    import urllib.request
    with urllib.request.urlopen(url) as response:
        content = response.read()
        details['type'] = type(content)
        details['content'] = content
        details['utf8 content'] = content.decode("utf-8")
    print("Body response:")
    for keys, values in details.items():
        print("\t- {}: {}".format(keys, values))
