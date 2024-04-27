from django.urls import path
from veg import views

urlpatterns = [
    path("", views.recipes, name="recipes"),
    
]
