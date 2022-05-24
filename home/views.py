import django
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.
# def home(request):
#     return render(request, 'home/welcome.html', {'today': datetime.today()})

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'