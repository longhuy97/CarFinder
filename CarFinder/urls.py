"""CarFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from account import views
from django.contrib.auth import views as auth_views
from post import views as post_views



urlpatterns = [
    path('', TemplateView.as_view(template_name='page/base.html')),  
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name="account/login.html"), name='login'),
    path('register/', views.register, name='register'),
    # path('post/', post_views.PostView, name='post'),
    path('post/', include('post.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
