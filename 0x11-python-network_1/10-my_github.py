#!/usr/bin/python3
"""Display user credential from GITHUB"""


import requests
from sys import argv
from requests.auth import HTTPBasicAuth


def usr_github_cred(user: str, passw: str):
    """
    GitHub credentials (username and password) and
    uses the GitHub API to display your id
    Args:
        user -> username
        pass -> password or Access token password
    """
    api = "https://api.github.com/user"
    header = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": f"Bearer {passw}"
            }

    auth = HTTPBasicAuth(user, passw)
    resp = requests.get(api, headers=header, auth=auth)
    return (resp.json().get('id'))


if __name__ == "__main__":
    print(usr_github_cred(argv[1], argv[2]))
