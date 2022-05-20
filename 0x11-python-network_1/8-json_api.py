#!/usr/bin/python3
"""
sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""

from sys import argv
import requests

if __name__ == "__main__":
    URL = "http://0.0.0.0:5000/search_user"
    print(len(argv))
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    data = {"q": q}
    try:
        response = requests.post(URL, data)
        data_json = response.json()
        id = data_json["id"]
        name = data_json["name"]
        if len(data_json) != 0:
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    except Exception as err:
        print("Not a valid JSON")
