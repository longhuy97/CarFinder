from django.urls import path
from django.http import HttpResponse
from post import views

urlpatterns = [
    path('list/',views.PostView),
    path('insert/', views.Insert_post, name='insert_post')
]
