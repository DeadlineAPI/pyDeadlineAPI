import abc
import re
from urllib.parse import urlparse

import json
import jsonschema

class Validator():
    def __init__(self) -> None:
        pass

    def validate(self,s) -> None:
        """
        Abstract method. Overwrite and implement the validation logic.
        """

        raise NotImplementedError

class Validator0_1(Validator, abc.ABC):
    def __init__(self) -> None:
        self.schema = json.load(open("0.1.json"))
        super().__init__()


    def _isURL(self,s) -> bool:
        try:
            result = urlparse(s)
            return all([result.scheme, result.netloc])
        except:
            return False

    def _isTwitter(self,s) -> bool:
        return s[0] == '@' and len(s) > 1

    def _isEmail(self,s) -> bool:
        return True

    def _isAPIVersion(self,s) -> bool:
        s = s.split('.')
        if len(s) <= 1:
            return False
        try:
            int(s[0])
            int(s[1])
            return True
        except:
            return False

    
    def _validate(self,dat) -> None:
        if dat["endpointurl"]:
            if not self._isURL(dat["endpointurl"]):
                raise Exception("endpointurl is not an url!")

        

    
    def validate(self, s) -> None:
        """
        validate: Throws error if something is no valid. If it does not throw any
        error, everything is alright.
        params:
        s: The DeadlineAPI JSON string
        """

        dat = json.loads(s)
        if dat["api"] == "0.1":
            jsonschema.validate(dat,self.schema)
            return
        else:
            raise Exception("The \"API\" field is either not present or contains a other API!")


        