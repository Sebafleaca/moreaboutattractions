from django.urls import path

from . import views


app_name = 'attractions'

urlpatterns = [
    path('', views.home, name='attractions'),
]