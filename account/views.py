from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView


class SiteLoginView(LoginView):
    template_name = 'login.html'