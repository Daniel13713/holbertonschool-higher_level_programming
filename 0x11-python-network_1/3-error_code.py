#!/usr/bin/python3
"""What's my status?"""

from urllib import request, parse
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    URL = argv[1]
    try:
        with request.urlopen(URL) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
