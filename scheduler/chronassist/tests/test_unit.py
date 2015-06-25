'''
Created on 24-Jun-2015

@author: anshul
'''
from django.test import TestCase
import unittest

from chronassist import views
from django.core.urlresolvers import resolve
from django.http.request import HttpRequest

class SimpleUnitTest(TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_root_url_resolves_to_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, views.index, "Functions do not match for Root URL")

    def test_homepage_returns_correct_html(self):
        request = HttpRequest()
        response = views.index(request)
        
        self.assertTrue(response.content.startswith(b'\n<!DOCTYPE html>'), response.content.decode())
        #I don't know how to make unit test ignore newlines.
        
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        
    def test_root_url_contains_form(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()