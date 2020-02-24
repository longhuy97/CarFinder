from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import UpPost

# Create your views here.
def PostView(request):
    return render(request,'post/post.html')

def Insert_post(request:HttpRequest):
    post = UpPost(topic = request.POST['title'])
    post.save()
    return redirect('/post/list/')
