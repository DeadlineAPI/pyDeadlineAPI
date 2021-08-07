

from urllib.parse import urlparse
import json

import jsonschema

def _is_url(s) -> bool:
        try:
            result = urlparse(s)
            return all([result.scheme, result.netloc])
        except:
            raise Exception(f"{s} is no valid url.")

def _is_twitter(s) -> bool:
    if not s[0] == '@' and len(s) > 1:
        raise Exception(f"{s} is no valid twitter account")

def _is_email(s) -> bool:
    pass

def _is_api_version(s) -> bool:
    splitted = s.split('.')
    if len(splitted) <= 1:
        raise Exception(f"A valid api version must have at least 2 two parts but {s} has less.")
    try:
        int(splitted[0])
        int(splitted[1])
    except:
        raise Exception(f"A valid api version must consist of two numbers but {s} does not.")

def _is_valid_date(s) -> bool:
    # TODO
    return True

def _is_valid_deadline(s) -> bool:
    # TODO
    return True

def _is_valid_schema_by_jsonobj(jsonobj) -> bool:
    schema = json.load(open("schema_0.1.json"))
    jsonschema.validate(jsonobj,schema)
