

class Location():
    def __init__(self,jsonobj,ignoreValidationErrors=False) -> None:

        if 'virtual' in jsonobj:
            self.virtual = jsonobj['virtual']
        else:
            raise Exception("virtual field is mandatory but not present!")

        if 'country' in jsonobj:
            self.country = jsonobj['country']
        elif self.virtual:
            pass
        else:
            raise Exception("country field is mandatory for non-virtual conferences but not present!")

        if 'city' in jsonobj:
            self.city = jsonobj['city']
        elif self.virtual:
            pass
        else:
            raise Exception("city field is mandatory for non-virtual conferences but not present!")

        if 'lat' in jsonobj:
            self.lat = float(jsonobj['lat'])
        if 'lon' in jsonobj:
            self.lon = float(jsonobj['lon'])
        