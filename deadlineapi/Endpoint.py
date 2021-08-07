

from deadlineapi.DeadlineObject import DeadlineObj
from deadlineapi.Validation import _is_api_version
from deadlineapi.Validation import _is_url

class Endpoint():
    def __init__(self,jsonobj) -> None:


        if 'api' in jsonobj:
            _is_api_version(jsonobj['api'])
            self.api = jsonobj['api']
        else:
            raise Exception("api field is mandatory but not present!")
        
        self.api_compatibility = []
        if 'api_compatibility' in jsonobj:
            for i in jsonobj['api_compatibility']:
                _is_api_version(jsonobj['api'])
                self.api_compatibility.append(i)


        if 'endpointname' in jsonobj:
            self.endpointname = jsonobj['endpointname']
            self.name = self.endpointname
        else:
            raise Exception("endpointname field is mandatory but not present!")

        if 'endpointurl' in jsonobj:
            _is_url(jsonobj['endpointurl'])
            self.endpointurl = jsonobj['endpointurl']
        else:
            self.endpointurl = None

        if 'endpointlogo' in jsonobj:
            _is_url(jsonobj['endpointlogo'])
            self.endpointlogo = jsonobj['endpointlogo']
        else:
            self.endpointlogo = None

        self.deadlines = []
        if 'deadlines' in jsonobj:
            for i in jsonobj['deadlines']:
                self.deadlines.append(DeadlineObj(i))


