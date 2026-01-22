from django.test import TestCase, Client
from django.urls import reverse

class PortfolioTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/index.html')

    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/page1.html')

    def test_merak_page(self):
        response = self.client.get(reverse('merak'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/coming_soon.html')

    def test_learning_journey_page(self):
        response = self.client.get(reverse('learning_journey'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/about_me.html')
