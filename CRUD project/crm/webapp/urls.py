from django.urls import path #the path function will help us create a url

# . means to look in the same directory
from . import views
#necessary whenever we need to setup a url file

urlpatterns = [
    #first parameter will be empty since it will be the home page
    #last parameter preferrred to have the same argument of the first parameter for consistency
    path('', views.home, name=""), 


]