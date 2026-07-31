#!/bin/bash
# Sends a GET request following redirects and displays the body only if the final status is 200
[ "$(curl -s -L -o /dev/null -w '%{http_code}' "$1")" = "200" ] && curl -s -L "$1"
