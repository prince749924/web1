from django.test import TestCase
from django.urls import reverse , resolve
from .views import *

# Create your tests here.
class Testurl(TestCase):
    def test_login(self):

        # booking = pass
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)
    
    def test_register(self):

        # booking = pass
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)
    
    def test_customerview(self):

        # booking = pass
        url = reverse('customerview')
        self.assertEqual(resolve(url).func, customerview)
    
    def test_dashboard(self):

        # booking = pass
        url = reverse('dash')
        self.assertEqual(resolve(url).func, dashboard)
    