from django.urls import path

from . import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user_view, name='user'),
]