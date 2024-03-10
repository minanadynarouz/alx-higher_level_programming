#!/bin/bash
# request that courses server to respond with a message containing You got me!

curl -sLX PUT -H "origin:AlxSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
