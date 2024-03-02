#!/usr/bin/python3
"""Script to fetch URL using requests package"""

import requests
from sys import argv


def display_err(url):
    req = requests.get(url)

    if int(req.status_code) >= 400:
        return ("Error code: {}".format(req.status_code))

    return (req.text)


if __name__ == "__main__":
    print(display_err(argv[1]))
