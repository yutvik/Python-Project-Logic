from django.shortcuts import render

# Create your views here.
def recipes(request):
    return render(request,"recipe.html")