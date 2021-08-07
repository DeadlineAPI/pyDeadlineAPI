



from api.Contact import Contact
from api.Location import Location
from api.Validation import _is_url, _is_valid_date, _is_valid_deadline

class DeadlineObj():

    def __init__(self,jsonobj):
        if 'name' in jsonobj:
            self.name = jsonobj['name']
        else:
            raise Exception("name field is mandatory but not present!")

        self.categories = []
        if 'categories' in jsonobj:
            for i in jsonobj['categories']:
                self.categories.append(i)

        if 'location' in jsonobj:
            self.location = Location(jsonobj['location'])
        else:
            raise Exception("location field is mandatory but not present!")

        if 'contact' in jsonobj:
            self.contact = Contact(jsonobj['contact'])
        else:
            raise Exception("contact field is mandatory but not present!")
        
        if 'startdate' in jsonobj:
            _is_valid_date(jsonobj['startdate'])
            self.startdate = jsonobj['startdate']
        else:
            raise Exception("startdate field is mandatory but not present!")

        if 'deadline' in jsonobj:
            _is_valid_deadline(jsonobj['deadline'])
            self.deadline = jsonobj['deadline']
        else:
            raise Exception("deadline field is mandatory but not present!")

        if 'shortname' in jsonobj:
            self.shortname = jsonobj['shortname']

        if 'logo' in jsonobj:
            _is_url(jsonobj['logo'])
            self.logo = jsonobj['logo']

        if 'cfpurl' in jsonobj:
            _is_url(jsonobj['cfpurl'])
            self.cfpurl = jsonobj['cfpurl']

        if 'confurl' in jsonobj:
            _is_url(jsonobj['confurl'])
            self.confurl = jsonobj['confurl']

        if 'enddate' in jsonobj:
            _is_valid_date(jsonobj['enddate'])
            self.enddate = jsonobj['enddate']

        if 'pagelimit' in jsonobj:
            self.pagelimit = int(jsonobj['pagelimit'])

