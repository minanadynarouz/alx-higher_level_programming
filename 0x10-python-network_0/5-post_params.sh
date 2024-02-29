#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=%20I%20will%20always%20be%20here%20for%20PLD" $1
