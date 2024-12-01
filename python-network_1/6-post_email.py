#!/usr/bin/python3
"""
Script that takes URL and email as input, sends POST request using requests
package, and displays the response body.
"""
import requests
import sys


def post_email(url, email):
    """
    Send POST request to URL with email parameter and print response.

    Args:
        url (str): The URL to send the POST request to
        email (str): The email to be sent as a parameter

    Returns:
        None. Prints the response body to stdout.
    """
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
