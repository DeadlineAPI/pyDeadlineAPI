
import json
import os
import logging

import requests
import jsonschema

import deadlineapi




logger = logging.getLogger("pyDeadlineAPI")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

logger.info(f"Running version {deadlineapi.__version__()}")


def main():

    directory = deadlineapi.Loader.load_directory_by_url()
    for endpoint in directory:
        print(f"Endpoint is compatible to: {endpoint.api_compatibility}")
        print(f"Deadlines provide by {endpoint.name}:")
        for d in endpoint.deadlines:
            print(f"{d.name}: {d.deadline}")
            
if __name__ == "__main__":
    main()
