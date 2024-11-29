#!/usr/bin/python3
"""
Script that sends a request to a URL and displays the X-Request-Id header value.
Uses urllib package to handle HTTP requests and sys for argument parsing.
"""
import urllib.request
import sys


def get_request_id(url):
    """
    Sends GET request to URL and prints X-Request-Id header value.

    Args:
        url (str): The URL to send the request to

    Returns:
        None. Prints the X-Request-Id header value to stdout.
    """
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))


if __name__ == "__main__":
    url = sys.argv[1]
    get_request_id(url)
