#!/usr/bin/python3
"""What's my status?"""

import requests

URL = "https://intranet.hbtn.io/status"
with requests.get(URL) as response:
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
