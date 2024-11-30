#!/usr/bin/python3
import sys
import requests

# Get the URL and email from the command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the 'email' parameter
data = {'email': email}

# Send a POST request to the URL with the email parameter
response = requests.post(url, data=data)

# Print the response body
print(response.text)

