from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegistrationForm
from django.http import HttpResponseRedirect

# def LoginView(request):
#     return render(request, 'account/login.html')

# class Resfrener(TemplateView):
#     template_name = 'account/register.html'

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    return render(request, 'account/register.html', {'form': form})
