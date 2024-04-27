# from audioop import reverse
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    person = [
        {'name':'Hari','Age':9},
        {'name':'Shreejit','Age':10},
        {'name':'Jell','Age':22},
        {'name':'Varni','Age':12},
        {'name':'Yutvik','Age':24},
        
    ]
    Vegetable = ["Potato","Tomato",]
    for peopal in person:
        print(peopal)
    return render(request,"index.html",context = {"page":"Live Project",'person':person}) 


def Contact(request):
    contact = {"page": "contact"}

    return render(request, "contact.html", contact)


def About(request):
    about = {"page":"about"}

    return render(request, "about.html",about)


def Success(rqeuest):
    
    print("*" ,10)
    return HttpResponse("<ht>This Page Success Page</h1>")

def Filed(request):
    pass
