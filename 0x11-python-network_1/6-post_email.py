#!/usr/bin/python3
"""
sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""

from sys import argv
import requests

if __name__ == "__main__":
    URL = argv[1]
    email = argv[2]
    data = {
        "email": email
    }
    response = requests.post(URL, data)
    print(response.text)
