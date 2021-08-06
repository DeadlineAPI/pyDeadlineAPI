
import unittest
from validators.Validator import Validator0_1


class TestValidator0_1(unittest.TestCase):

    validator = Validator0_1()


    def test_isURL(self):
        self.assertEqual(True,self.validator._isURL("http://google.de"))
        self.assertEqual(True,self.validator._isURL("https://google.de"))
        self.assertEqual(True,self.validator._isURL("http://subdomain.google.de"))

        self.assertEqual(False,self.validator._isURL("google.de"))
        self.assertEqual(False,self.validator._isURL("google"))

    def test_isTwitter(self):
        self.assertEqual(True,self.validator._isTwitter("@test"))
        self.assertEqual(True,self.validator._isTwitter("@t"))
        self.assertEqual(True,self.validator._isTwitter("@HalloWelt"))

        self.assertEqual(False,self.validator._isTwitter("test"))
        self.assertEqual(False,self.validator._isTwitter("@"))

    def test_isEMail(self):
        # TODO
        pass

    def test_isAPIVersion(self):
        self.assertEqual(True,self.validator._isAPIVersion("0.1"))
        self.assertEqual(True,self.validator._isAPIVersion("0112.1112"))
        
        
        self.assertEqual(False,self.validator._isAPIVersion("01"))
        self.assertEqual(False,self.validator._isAPIVersion("1000"))
        self.assertEqual(False,self.validator._isAPIVersion("10.a"))
        self.assertEqual(False,self.validator._isAPIVersion("a"))
        self.assertEqual(False,self.validator._isAPIVersion("b.b"))
        