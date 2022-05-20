#!/usr/bin/python3
"""What's my status?"""

from urllib.request import urlopen
from sys import argv


URL = argv[1]
with urlopen(URL) as response:
    print(response.headers["X-Request-Id"])
