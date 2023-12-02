#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    with requests.get('https://alx-intranet.hbtn.io/status') as res:
        output = """Body response:
    - type: {}
    - content: {}""".format(type(res.text), res.text)
        print(output)
