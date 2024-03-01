#!/usr/bin/python3
"""Script to fetch URL"""

from urllib import request, error


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with request.urlopen(url) as response:
            res = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(res)))
            print("\t- content: {}".format(res))
            print("\t- utf8 content: {}".format(res.decode('utf-8')))
    except error.URLError:
        print("Cannot connect to {}".format(url))
