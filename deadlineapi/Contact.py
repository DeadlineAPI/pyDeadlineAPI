
from deadlineapi.Validation import _is_email, _is_twitter

class Contact():
    def __init__(self,jsonobj) -> None:

        if 'email' in jsonobj:

            _is_email(jsonobj['email'])
            self.email = jsonobj['email']


        if 'twitter' in jsonobj:
            _is_twitter(jsonobj['twitter'])
            self.twitter = jsonobj['twitter']
