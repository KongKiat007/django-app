from django.test import TestCase
from django.urls import reverse

class HomePageViewTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'index.html')