#!/usr/bin/python3
"""
Module to fetch and display status from ALU Intranet.

This script demonstrates how to use urllib to fetch
a status page and display its contents with detailed information.
"""
import urllib.request


def fetch_status():
    """
    Fetch status from https://alu-intranet.hbtn.io/status.

    Displays the response details using specified formatting.
    """
    url = 'https://alu-intranet.hbtn.io/status'
    
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    
    except urllib.error.URLError as e:
        print("Error fetching status: {}".format(e))


if __name__ == "__main__":
    fetch_status()
