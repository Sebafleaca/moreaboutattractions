import random

from django.shortcuts import render

from .models import Attraction, Favorite
from . import googleapi


def home(request):
    return render(request, 'attractions/home.html')

def nearby(request):

    if request.method == 'POST':

        actual_location = request.POST['location']
        
        latitude, longitude = actual_location.split(',')
        maps_api = googleapi.GoogleApi(latitude, longitude)
        
        received_data = maps_api.mock_api()

        already_in = Attraction

        for elem in received_data:
            if not already_in.objects.get(name=received_data[elem]['name']):
                attraction = Attraction.objects.create()
                attraction.name = received_data[elem]['name']
                attraction.position = f"{latitude}, {longitude}"
                attraction.saved = False
                attraction.save()

    return render(request, 'attractions/nearby.html')

def found(request):
    
    api_response = googleapi.GoogleApi(0,0)
    google_response = api_response.send_request()

    all_attractions = Attraction.objects.all()
    context = {
        'status': google_response['status'],
        'message': google_response['error_message'],
        'all_attractions': all_attractions
    }

    return render(request, 'attractions/found.html', context)

def attraction(request, attraction_number):
    attraction = Attraction.objects.get(id=attraction_number)
    context = {
        'attraction_name': attraction.name,
        'attraction_position': attraction.position,
        'attraction_saved': attraction.saved,
    }

    if request.method == 'POST':        
        if attraction.saved:
            Favorite.objects.filter(attraction=attraction.name).delete()
            attraction.saved = False
            attraction.save()
        else:            
            new_favorite = Favorite.objects.create()
            new_favorite.attraction = str(attraction)
            new_favorite.rating = random.randrange(1, 10)
            new_favorite.save()
            attraction.saved = True
            attraction.save()


    return render(request, 'attractions/attraction.html', context)

def favorites(request):
    favorite_attractions = Favorite.objects.all().values()

    context = {
        'favorite_attractions': favorite_attractions
    }
    return render(request, 'attractions/favorites.html', context)