#!/usr/bin/python3
"""
sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""

from sys import argv
import requests

if __name__ == "__main__":
    URL = argv[1]
    response = requests.get(URL)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
