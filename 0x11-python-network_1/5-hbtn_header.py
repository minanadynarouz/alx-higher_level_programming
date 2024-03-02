#!/usr/bin/python3
"""Script to fetch URL using requests package"""

import requests
from sys import argv


def display_header_requests(url):
    try:
        req = requests.get(url)
        print(req.headers['X-Request-Id'])
    except Exception as e:
        return e


if __name__ == "__main__":
    display_header_requests(argv[1])
