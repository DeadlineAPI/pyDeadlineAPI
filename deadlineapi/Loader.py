
import json
import requests
import os

import deadlineapi.Endpoint
from deadlineapi.Validation import _is_valid_schema_by_jsonobj,_is_url

def load_endpoint_by_json(jsonobj):
    _is_valid_schema_by_jsonobj(jsonobj)
    return deadlineapi.Endpoint(jsonobj)

def load_endpoint_by_string(s):
    jsonobj = json.loads(s)
    return load_endpoint_by_json(jsonobj)

def load_endpoint_by_path(path):
    return load_endpoint_by_string(open(path,'r').read())

def load_endpoint_by_url(url):
    _is_url(url)
    return load_endpoint_by_string(requests.get(url=url,timeout=5).text)



DEFAULT_DIRECTORY_URL = "https://directory.deadlineapi.org/directory.json"

def load_directory_by_string(s):
    directory = json.loads(s)
    endpoints = []
    for k in directory:
        print(f"Loading endpoint {k} with url {directory[k]}")
        try:
            endpoints.append(load_endpoint_by_url(directory[k]))
        except:
            print(f"Failed to load endpoint {k}...")
    return endpoints

def load_directory_by_url(url=DEFAULT_DIRECTORY_URL):
    return load_directory_by_string(requests.get(url=url,timeout=5).text)
    
def load_directory_by_path(path):
    return load_directory_by_string(open(path,'r').read())