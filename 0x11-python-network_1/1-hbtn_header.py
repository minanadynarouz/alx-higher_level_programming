#!/usr/bin/python3
"""Script to fetch URL"""

from urllib import request, error
from sys import argv


def display_header(url: str) -> str:
    """
    Send request to url which is received as input in function
    return the response as str
    Args:
        url (str): The url to be fetched
    """

    try:
        with request.urlopen(url) as response:
            return (response.headers['X-Request-Id'])
    except error.URLError as e:
        return (e.reason)

if __name__ == "__main__":
    print(display_header(argv[1]))
