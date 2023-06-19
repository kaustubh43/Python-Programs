from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


## Function based View
# def home(request):
#     return render(request, 'home/welcome.html', {'today': datetime.today()})


class Authorize(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = './admin'


# @login_required(login_url='/admin')
# def authorize(request):
#     return render(request, 'home/authorize.html', {})
