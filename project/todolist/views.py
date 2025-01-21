from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    person = [{
        'name': "test",
        'age': 20
    },
    {
        'name': "test2",
        'age': 30
    },
    {
        'name': "test3",
        'age': 40
    },
    {
        'name': "test4",
        'age': 50
    },
    {
        'name': "test5",
        'age': 60
    }
    ]
    context = {'name': "Home Page",
               'persons': person}
    return render(request, 'home.html', context)

def index(request):
    return HttpResponse("This is a index function")

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return HttpResponse("This is a about function") 