'''
Created on 24-Jun-2015

@author: anshul
'''
from django.test import TestCase
import unittest

from chronassist import views
from django.core.urlresolvers import resolve
from django.http.request import HttpRequest
from django.template.loader import render_to_string

from chronassist.models import Item
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
        
    def test_user_can_post(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new text item'
        #Make a request
        response = views.index(request)
        
        #Count the number of objects in DB
        self.assertEqual(Item.objects.all().count(), 1)
        new_item = Item.objects.all()[0]
        
        self.assertEqual(new_item.item, 'A new text item', 
                         "Expected {text} but got {text2}".format(text='A new text item', 
                                                                  text2=new_item.item))
        
        self.assertIn('A new text item', response.content.decode())
        expected_html = render_to_string(
                                         'chronassist/base.html',
                                         {'new_item_text': request.POST['item_text']}
                                         )
        self.assertEqual(response.content.decode(), 
                         expected_html) 
        #"Expected HTML and returned HTML do not match\n[Expected]\n{expect}\n[Received]\n{recv}".format(
        #expect=expected_html, recv=response.content.decode()))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()