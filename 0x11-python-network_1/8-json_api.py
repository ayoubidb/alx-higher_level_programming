#!/usr/bin/python3
"""
    Sends a POST request to http://0.0.0.0:5000/search_user
    with a given letter.
"""
import requests
import sys

if __name__ == "__main__":
    query = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": query}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
