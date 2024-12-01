#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to a search API
The letter is sent in the variable q
If no argument is given, q = ""
Display the id and name if JSON response is properly formatted and not empty
Display No result if JSON is empty
Display Not a valid JSON if response is not valid JSON
"""
import requests
import sys


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {'q': letter}

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
        r_json = r.json()
        if r_json:
            print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
