#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -s -X POST --data "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
