#!/usr/bin/python3
"""What's my status?"""

from urllib.request import Request, urlopen
from sys import argv


URL = argv[1]
req = Request(URL)
with urlopen(req) as response:
    print(response.headers["X-Request-Id"])
