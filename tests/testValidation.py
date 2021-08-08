
import unittest
from deadlineapi.Validation import _is_url, _is_email, _is_twitter, _is_api_version


class TestValidation(unittest.TestCase):
    
    def test_is_url(self):
        _is_url("http://google.de")
        _is_url("https://google.de")
        _is_url("http://subdomain.google.de")

        _is_url("google.de")
        _is_url("google") # ???

        self.assertTrue(True)

    def test_is_twitter(self):
        _is_twitter("@test")
        _is_twitter("@t")
        _is_twitter("@HalloWelt")

        with self.assertRaises(Exception):
            _is_twitter("test")
            _is_twitter("@")
        
        self.assertTrue(True)

    def test_is_email(self):
        # TODO
        self.assertTrue(True)
        pass

    def test_is_api_version(self):
        _is_api_version("0.1")
        _is_api_version("0112.1112")
        
        with self.assertRaises(Exception):
            _is_api_version("01")
            _is_api_version("1000")
            _is_api_version("10.a")
            _is_api_version("a")
            _is_api_version("b.b")
        
        self.assertTrue(True)
        