#!/usr/bin/env python3

import requests

def json_conv(poke_api):
    # send a get request to poke_api
    try:
        json2python = requests.get(poke_api).json()
        # the value of json2python is the whole dictionary of bulbasaur!
        print(json2python)
        return json2python
    except:
        print("Invalid URL provided. Please try again.")

