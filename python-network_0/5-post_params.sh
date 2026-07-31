#!/bin/bash
# Sends a POST request with the required parameters and displays the body of the response
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
