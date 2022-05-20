#!/usr/bin/python3
"""What's my status?"""

import requests
from sys import argv

if __name__ == "__main__":
    URL = argv[1]
    with requests.session() as session:
        response = session.get(URL)
        print(response.headers["X-Request-Id"])
