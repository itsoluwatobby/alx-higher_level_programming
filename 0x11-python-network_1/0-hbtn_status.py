#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        res = response.read()
        output = """Body response:
            - type: {}
            - content: {}
            - utf8 content: {}""".format(type(res), res, res.decode('utf-8'))
        print(output)
