from django.test import TestCase
from django.test import Client
from django.urls import reverse


# Create your tests here.


class SomeTests(TestCase):
    def test_math(self):
        """
        put docstrings in your tests
        """
        self.assertEqual(2 + 2, 4)


class TemplateTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        url = reverse('home_url')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, '<title>Home page</title>')
        self.assertTemplateUsed(response, 'hello/home.html')
        self.assertContains(response, '<h2>42 Coffee Cups Test Assignment</h2>')
        self.assertContains(response, '<div>Name: Maxim</div>')
        self.assertContains(response, '<div>Last name: Hordiychuck</div>')

        bio = """<div>Bio:
                <p>Born in KK, he graduated from school in 2015. He studied in Lutsk.
                    Hobbies history, programming, guitar.</p>
            </div>"""
        self.assertContains(response, bio)

        self.assertContains(response, '<div>Contacts: +068*******</div>')
        self.assertContains(response, '<div>email: OA3IC.QV@gmail.com</div>')
        self.assertContains(response, '<div>Jabber: max_hordiychuck@42cc.co</div>')
        self.assertContains(response, '<div>Skype: e9ec196de1ffa713</div>')

        other_contacts = """<div>Other contacts:
                <p>None</p>
            </div>"""
        self.assertContains(response, other_contacts)