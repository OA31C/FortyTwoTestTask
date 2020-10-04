from django.test import TestCase
from ..models import Person


# Create your tests here.
class TestModelPerson(TestCase):

    @classmethod
    def setUpTestData(cls):
        Person.objects.create(
            name='Max',
            last_name='Hordiychuck',
            date_of_birth='1997-12-22',
            bio='Born in KK, he graduated from school in 2015. He studied in Lutsk.'
                'Hobbies history, programming, guitar.',
            contacts='+068*******',
            email='OA3IC.QV@gmail.com',
            jabber='max_hordiychuck@42cc.co',
            skype='e9ec196de1ffa713',
            other_contacts=None
        )

    def test_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Name')

    def test_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)

    def test_last_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'Last Name')

    def test_last_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 30)

    def test_check_first_upper_letter(self):
        person = Person.objects.get(id=1)
        self.assertEqual(person.name, person.name.upper())
        self.assertEqual(person.last_name, person.last_name.upper())

    def test_date_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'Date of birth')

    def test_bio_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'Bio')

    def test_contacts_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('contacts').verbose_name
        self.assertEqual(field_label, 'Contacts')

    def test_contacts_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('contacts').max_length
        self.assertEqual(max_length, 13)

    def test_email_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'Email')

    def test_email_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('email').max_length
        self.assertEqual(max_length, 40)

    def test_jabber_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('jabber').verbose_name
        self.assertEqual(field_label, 'Jabber ID')

    def test_jabber_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('jabber').max_length
        self.assertEqual(max_length, 40)

    def test_skype_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('skype').verbose_name
        self.assertEqual(field_label, 'Skype ID')

    def test_skype_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('contacts').max_length
        self.assertEqual(max_length, 20)

    def test_other_contacts_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('other_contacts').verbose_name
        self.assertEqual(field_label, 'Other contacts')

