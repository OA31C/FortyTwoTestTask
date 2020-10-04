from django.shortcuts import render
from apps.person.models import Person


# Create your views here.
def home(request):
    person = Person.objects.get(id=1)
    return render(request, 'person/home.html', context={'person': person})
