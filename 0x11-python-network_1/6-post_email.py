#!/usr/bin/python3
"""Script to fetch URL using requests package"""

import requests
from sys import argv


def display_body(url, email):
    try:
        data = {}
        data['email'] = email
        req = requests.post(url, data=data)
        return (req.text)
    except Exception as e:
        return e


if __name__ == "__main__":
    print(display_body(argv[1], argv[2]))
