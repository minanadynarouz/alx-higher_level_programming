#!/usr/bin/python3

"""Add all arguments to a list and save them to a .json"""
from sys import argv
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    try:
        oldContent = load_from_json_file("add_item.json")
    except FileNotFoundError:
        oldContent = []

    oldContent += argv[1:]

    save_to_json_file(oldContent, "add_item.json")


if __name__ == '__main__':
    main()
