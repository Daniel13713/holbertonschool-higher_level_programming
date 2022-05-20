#!/usr/bin/python3
"""What's my status?"""

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    URL = argv[1]
    email = argv[2]
    params = {
        "email": email
    }
    query = parse.urlencode(params)
    data = query.encode("utf-8")
    with request.urlopen(URL, data) as response:
        print(response.read().decode("utf-8"))
