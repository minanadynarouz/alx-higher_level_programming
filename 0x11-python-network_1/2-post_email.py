#!/usr/bin/python3
"""Script to fetch URL"""

from urllib import request, parse, error
from sys import argv


def add_mail_param(url: str, email: str) -> str:
    """
    Send request to url which is received as input in function
    add email as param
    Args:
        url (str): The url to be fetched
        email (str): email to be sent in params
    """

    data = {'email': email}
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url, data, method="POST")
    try:
        with request.urlopen(req) as response:
            return response.read().decode("utf-8")
    except error.URLError as e:
        return e.reason

if __name__ == "__main__":
    print(add_mail_param(argv[1], argv[2]))
