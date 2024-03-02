#!/usr/bin/python3
"""Script to fetch URL using requests package"""

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        res = requests.get(url)
        res_content = res.content.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(res_content)))
        print("\t- content: {}".format(res_content))
    except error.URLError:
        print("Cannot connect to {}".format(url))
