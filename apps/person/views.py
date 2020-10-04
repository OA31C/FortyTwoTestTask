from django.shortcuts import render

data = {'name': 'Max',
        'last_name': 'Hordiychuck',
        'date_of_birth': '1997-12-22',
        'bio': 'Born in KK, he graduated from school in 2015. He studied in Lutsk.'
               'Hobbies history, programming, guitar.',
        'contacts': '+068*******',
        'email': 'OA3IC.QV@gmail.com',
        'jabber': 'max_hordiychuck@42cc.co',
        'skype': 'e9ec196de1ffa713',
        'other_contacts': 'None'
        }


# Create your views here.
def home(request):
    return render(request, 'person/home.html', context={'data': data})
