#!/usr/bin/python3
"""Script to fetch URL"""

import urllib.request as Req


if __name__ == '__main__':
    with Req.urlopen('https://alx-intranet.hbtn.io/status') as response:
        res = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utff8 content: {}".format(res.decode('utf-8')))
