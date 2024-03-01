#!/usr/bin/python3
"""Script to fetch URL"""

from urllib import request, parse, error
from sys import argv


def get_res(url: str) -> str:
    """
    Send request to url which is received as input in function
    get body of the response
    Args:
        url (str): The url to be fetched
    """
    try:
        with request.urlopen(url) as response:
            return response.read().decode("utf-8")
    except error.HTTPError as e:
        return "Error code: {}".format(e.code)


if __name__ == "__main__":
    print(get_res(argv[1]))
