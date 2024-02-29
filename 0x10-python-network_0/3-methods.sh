#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -sI OPTIONS $1 | grep -i "allow" | cut -d ":" -f 2
