#!/usr/bin/python3
"""What's my status?"""

import requests

if __name__ == "__main__":
    URL = "https://intranet.hbtn.io/status"
    with requests.session() as session:
        response = session.get(URL)
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
