# from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.


class MysnackTest(SimpleTestCase):

    def test_home(self):
        """
        Check for route to home page
        """
        expected = 200
        url = reverse('home')
        response = self.client.get(url)
        actual = response.status_code
        # assert expected == actual
        self.assertEquals(expected,actual)

    def test_for_about(self):
        """
        Check for route to about page
        """
        expected = 200
        url = reverse('about')

        response = self.client.get(url)
        actual = response.status_code

        self.assertEquals(expected,actual)

    

class Mytest(SimpleTestCase):
    """
    I examine that if made more than one class
    """
    def test_template_home(self):
        """
        Check for the right path to the desired page
        """
        url = reverse('home')
        response = self.client.get(url)
        actual= 'home.html'
        self.assertTemplateUsed(response,actual)
    
    def test_template_about(self):
        """
        Check for the right path to the desired page
        """
        url = reverse('about')
        response = self.client.get(url)
        actual= 'about.html'
        self.assertTemplateUsed(response,actual)
