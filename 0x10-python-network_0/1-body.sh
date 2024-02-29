#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -sL --fail -X GET $1
