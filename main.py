
import json
import os
import logging

import requests
import jsonschema

from validators.Validator import Validator0_1 



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
    validator = Validator0_1()
    try:
        validator.validate(open(os.path.join("test","test01.json"),'r').read())
        logger.info("Validation passed!")
    except:
        logger.info("Validation failed!")



if __name__ == "__main__":
    main()
