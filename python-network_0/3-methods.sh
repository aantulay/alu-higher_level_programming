#!/bin/bash
# Displays all HTTP methods the server accepts for the given URL
curl -s -X OPTIONS -D - -o /dev/null "$1" | grep -i "^Allow:" | cut -d: -f2 | sed 's/^ *//;s/\r$//'