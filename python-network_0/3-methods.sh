#!/bin/bash
# Script to display all HTTP methods the server accepts
curl -sX OPTIONS "$1" -I | grep "Allow:" | cut -d ':' -f 2 | sed 's/^ *//; s/ *$//'
