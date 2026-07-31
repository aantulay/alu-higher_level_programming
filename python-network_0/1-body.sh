#!/bin/bash
# Sends a GET request and displays the body only if the response status is 200
[ "$(curl -s -o /dev/null -w '%{http_code}' "$1")" = "200" ] && curl -s "$1"