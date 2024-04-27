from django.urls import path
from App import views
urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.Contact, name="contact"),
    path("about/", views.About, name="about"),
    
    
]
