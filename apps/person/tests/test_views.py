from django.test import TestCase
from django.test import Client
from django.urls import reverse


# Create your tests here.
class TestViewHome(TestCase):

    def setUp(self):
        self.client = Client()

    def test_checks_if_the_data_from_view_correct(self):
        url = reverse('home_url')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, '<title>Home page</title>')
        self.assertContains(response, '<h2>42 Coffee Cups Test Assignment</h2>')
        self.assertContains(response, response.context.get('data').get('name'))
        self.assertContains(response, response.context.get('data').get('last_name'))
        self.assertContains(response, response.context.get('data').get('bio'))

        self.assertContains(response, response.context.get('data').get('contacts'))
        self.assertContains(response, response.context.get('data').get('email'))
        self.assertContains(response, response.context.get('data').get('jabber'))
        self.assertContains(response, response.context.get('data').get('skype'))
        self.assertContains(response, response.context.get('data').get('other_contacts'))

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'person/home.html')