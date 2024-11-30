#!/usr/bin/python3
import sys
import requests

"""
A script that uses GitHub API with Basic Authentication to fetch and display
the user ID for a specified GitHub username and personal access token.
"""

def main():
    # Get GitHub username and personal access token (password) from command line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API URL to get user information
    url = "https://api.github.com/user"

    # Send GET request with Basic Authentication
    response = requests.get(url, auth=(username, token))

    # If the authentication is successful, print the user ID, otherwise print None
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print(None)

if __name__ == "__main__":
    main()

