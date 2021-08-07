
import json
import os
import logging

import requests
import jsonschema

import deadlineapi


VERSION_MAJOR = 0
VERSION_MINOR = 0
VERSION_PATCH = 1
VERSION = "v" + str(VERSION_MAJOR) + "." + str(VERSION_MINOR) + "." + str(VERSION_PATCH)

logger = logging.getLogger("pyDeadlineAPI")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

logger.info("Running version " + VERSION)


def main():
    directory = api.Loader.load_directory_by_url("https://directory.deadlineapi.org/directory.json")
    for endpoint in directory:
        print(f"Endpoint is compatible to: {endpoint.api_compatibility}")
        print(f"Deadlines provide by {endpoint.name}:")
        for d in endpoint.deadlines:
            print(f"{d.name}: {d.deadline}")
        

if __name__ == "__main__":
    main()
