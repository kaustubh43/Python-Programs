from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # The first parameter is the address of the webpage
    # path('authorize', views.Home.authorize)  # Function based view
    path('login', views.LoginInterfaceViews.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
