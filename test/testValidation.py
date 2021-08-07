
import unittest
from api.Validation import *


class TestValidation(unittest.TestCase):
    
    def test_isURL(self):
        self.assertEqual(True,_is_url("http://google.de"))
        self.assertEqual(True,_is_url("https://google.de"))
        self.assertEqual(True,_is_url("http://subdomain.google.de"))

        self.assertEqual(False,_is_url("google.de"))
        self.assertEqual(False,_is_url("google"))

    def test_isTwitter(self):
        self.assertEqual(True,_is_twitter("@test"))
        self.assertEqual(True,_is_twitter("@t"))
        self.assertEqual(True,_is_twitter("@HalloWelt"))

        self.assertEqual(False,_is_twitter("test"))
        self.assertEqual(False,_is_twitter("@"))

    def test_isEMail(self):
        # TODO
        pass

    def test_isAPIVersion(self):
        self.assertEqual(True,_is_api_version("0.1"))
        self.assertEqual(True,_is_api_version("0112.1112"))
        
        self.assertEqual(False,_is_api_version("01"))
        self.assertEqual(False,_is_api_version("1000"))
        self.assertEqual(False,_is_api_version("10.a"))
        self.assertEqual(False,_is_api_version("a"))
        self.assertEqual(False,_is_api_version("b.b"))
        