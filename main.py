
import json
import os
import logging

import requests
import jsonschema

import api



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
    endpoint = directory[0]
    print(endpoint.api_compatibility)
    for d in endpoint.deadlines:
        print(d.name)


if __name__ == "__main__":
    main()
