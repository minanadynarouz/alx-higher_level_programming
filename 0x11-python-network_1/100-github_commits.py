#!/usr/bin/python3
"""Script to fetch URL using requests package"""

import requests
from sys import argv


def git_commits(repo_name: str, ownerName: str):
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    req = requests.get(url)
    commits = req.json()

    try:
        for x in range(10):
            print("{}: {}".format(
                commits[x].get("sha"),
                commits[x].get("commit").get("author").get("name")))
    except IndexError:
        pass


if __name__ == "__main__":
    git_commits(argv[2], argv[1])
