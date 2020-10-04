from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(verbose_name='Name', max_length=30)
    last_name = models.CharField(verbose_name='Last Name', max_length=30)
    date_of_birth = models.DateField(verbose_name='Date of birth')
    bio = models.TextField(verbose_name='Bio')

    contacts = models.CharField(verbose_name='Contacts', max_length=13)
    email = models.EmailField(verbose_name='Email', max_length=40)
    jabber = models.CharField(verbose_name='Jabber ID', max_length=40)
    skype = models.CharField(verbose_name='Skype ID', max_length=20)
    other_contacts = models.TextField(verbose_name='Other contacts')

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.last_name = self.last_name.title()
        return super(Person, self).save(*args, **kwargs)
