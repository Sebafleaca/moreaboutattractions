"""moreaboutattractions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
=======


urlpatterns = [
    path('admin/', admin.site.urls),
    path('attractions/', include('attractions.urls')),
>>>>>>> 90a85c32f9b7f5752cf8218241efb9e93579ec17
]
