from django.urls import path

from . import views

urlpatterns = [
    path('home', views.HomeView.as_view()),
    # The first parameter is the address of the webpage
    # path('authorize', views.Home.authorize)  # Function based view
    path('authorize', views.Authorize.as_view())  # Class based views
]
