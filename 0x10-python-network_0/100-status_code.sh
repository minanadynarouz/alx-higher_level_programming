#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -o /dev/null -sIw "%{http_code}" "$1"
