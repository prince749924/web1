from .views import bookingfinal
from django.urls import reverse , resolve
from django.test import TestCase

# Create your tests here.
class testurl(TestCase):
    def test_booking(self):

        # booking = pass
        url = reverse('booking')
        self.assertEqual(resolve(url).func, bookingfinal)
