#!/usr/bin/python3
"""
Script that sends a POST request to a URL with an email parameter.
Uses urllib package to handle HTTP requests and sys for argument parsing.
Displays the response body decoded in UTF-8.
"""
import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """
    Sends POST request to specified URL with email parameter and prints response.

    Args:
        url (str): The URL to send the POST request to
        email (str): The email to be sent as a parameter

    Returns:
        None. Prints the response body to stdout.
    """
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
