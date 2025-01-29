#!/usr/bin/python3
"""
Module to send HTTP requests and handle response error codes.

This script takes a URL as an argument, sends a request,
and displays the response body or error code.
"""
import sys
import requests


def fetch_url_content(url):
    """
    Fetch content from the given URL and handle potential error codes.

    Args:
        url (str): The URL to send a request to.
    """
    try:
        # Send GET request
        response = requests.get(url)
        
        # Check if HTTP status code is >= 400
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            # Print response body for successful requests
            print(response.text)
    
    except requests.RequestException as e:
        # Handle any request-related exceptions
        print("Error: {}".format(e))


def main():
    """
    Main function to process URL from command-line arguments.
    """
    # Check if URL is provided as a command-line argument
    if len(sys.argv) > 1:
        url = sys.argv[1]
        fetch_url_content(url)


if __name__ == "__main__":
    main()
