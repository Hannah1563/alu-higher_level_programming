#!/bin/bash
# Script that displays the size of the response body from a URL
curl -s "$1" | wc -c
