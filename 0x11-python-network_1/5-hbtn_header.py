#!/usr/bin/python3
"""What's my status?"""

from sys import argv
import requests

if __name__ == "__main__":
    URL = argv[1]
    with requests.get(URL) as response:
        print(response.headers["X-Request-Id"])
