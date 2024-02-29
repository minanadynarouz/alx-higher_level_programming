#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -d "$(cat "$2")" -sX PORT --header "Content-Type: application/json" "$1"
