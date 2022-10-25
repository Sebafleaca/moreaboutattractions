from django.urls import path

from . import views


app_name = 'attractions'

urlpatterns = [
    path('', views.home, name='attractions'),
    path('nearby', views.nearby, name='nearby'),
    path('found', views.found, name='found'),
    path('favorites', views.favorites, name='favorites'),
]