#!/usr/bin/python3
import sys
import requests

"""
A script that sends a POST request to a specified URL with an email as a parameter.

Usage:
    ./6-post_email.py <URL> <email>

Args:
    URL: The URL where the POST request should be sent.
    email: The email address to be sent as a parameter in the POST request.
"""

def main():
    # Get the URL and email from the command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the 'email' parameter
    data = {'email': email}

    # Send a POST request to the URL with the email parameter
    response = requests.post(url, data=data)

    # Print the response body
    print(response.text)


if __name__ == "__main__":
    main()

