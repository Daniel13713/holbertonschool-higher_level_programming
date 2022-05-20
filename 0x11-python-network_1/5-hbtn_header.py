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
    print(response.headers.get("X-Request-Id"))
