#!/usr/bin/python3
"""What's my status?"""

from urllib.request import urlopen

URL = "https://intranet.hbtn.io/status"
with urlopen(URL) as response:
    content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode("utf-8")))
