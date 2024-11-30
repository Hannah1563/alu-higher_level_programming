#!/usr/bin/python3
"""
Script that takes in a URL, sends a request and displays the response body.
Handles urllib.error.HTTPError exceptions and displays the HTTP status code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
