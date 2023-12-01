#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}

    res = requests.post(req, data=values)
    print(res.text)
