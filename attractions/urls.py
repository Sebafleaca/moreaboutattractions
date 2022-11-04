from django.urls import path

from . import views


app_name = 'attractions'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:number>', views.attraction, name='attraction'),
    path('nearby', views.nearby, name='nearby'),
    path('found', views.found, name='found'),
    path('favorites', views.favorites, name='favorites'),
]