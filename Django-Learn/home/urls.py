from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home),
    # The first parameter is the address of the webpage
    path('authorize', views.authorize)
]
