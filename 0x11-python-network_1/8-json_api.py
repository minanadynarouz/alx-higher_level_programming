#!/usr/bin/python3
"""script that takes in a letter and sends a POST request"""


import requests
from sys import argv


def send_letter_port(letter=""):
    """Function to send letter in post request
    and return user name if valid
    return no valid words if not valid
    Args:
        letter -> default is empty string
        this is the letter to be sent.
    """

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    resp = requests.post(url, data=data)

    try:
        resp_json = resp.json()
        if len(resp_json) != 0:
            return ("[{}] {}".format(resp_json.get('id'), resp_json.get('name')))
        return ("No result")
    except Exception as e:
        return ("Not a valid JSON")

if __name__ == "__main__":
    if len(argv) == 2:
        print(send_letter_port(argv[1]))
    else:
        print(send_letter_port(""))
