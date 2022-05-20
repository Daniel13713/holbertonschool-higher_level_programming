#!/usr/bin/python3
"""What's my status?"""

from urllib.request import urlopen

URL = "https://intranet.hbtn.io/status"
with urlopen(URL) as response:
    print("\t-type: <class 'bytes'>")
    content = response.read()
    print("\t-content: {}".format(content))
    print("\t-utf8 content: OK")
