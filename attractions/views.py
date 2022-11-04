import random

from django.shortcuts import render
#from django.shortcuts import redirect

from .models import Attraction, Favorite
from .forms import LocationForm
from . import googleapi


def home(request):
    '''Render home page.'''
    return render(request, 'attractions/home.html')

def nearby(request):
    '''Render form to get location.'''
    if request.method == 'POST':
        location_form = LocationForm(request.POST)
    elif request.method == 'GET':
        location_form = LocationForm()
    else:
        raise NameError("/nearby/ doesn't get POST nor GET")

    return render(request, 'attractions/nearby.html', {'location_form': location_form})

def found(request):
    '''Send location to API, add results to database and display them.'''
    if request.method == 'POST':
        location_form = LocationForm(request.POST)
        
        if location_form.is_valid():
        
            actual_location = location_form.cleaned_data['coordinates']
            latitude, longitude = actual_location.split(', ')
            api_response = googleapi.GoogleApi(latitude, longitude)
        
            google_response = api_response.send_request()
            received_data = api_response.mock_api()

            for element in received_data:
                if not Attraction.objects.filter(name=received_data[element]['name']):
                    attraction = Attraction.objects.create()
                    attraction.name = received_data[element]['name']
                    attraction.position = f"{latitude}, {longitude}"
                    attraction.saved = False
                    attraction.save()
    
            all_attractions = Attraction.objects.all()

            context = {
                'status': google_response['status'],
                'message': google_response['error_message'],
                'all_attractions': all_attractions,
                'latitude': latitude,
                'longitude': longitude,
                'received_data': received_data,
            }
    else:
        #return redirect(nearby)
        raise NameError("/nearby/ doesn't get a POST request.")

    return render(request, 'attractions/found.html', context)

def attraction(request, number):
    attraction = Attraction.objects.get(id=number)

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

    context = {
        'attraction_name': attraction.name,
        'attraction_position': attraction.position,
        'attraction_saved': attraction.saved,
    }

    return render(request, 'attractions/attraction.html', context)

def favorites(request):

    if request.method == 'POST':
        favorite_attractions = Favorite.objects.all()

        context = {
            'favorite_attractions': favorite_attractions
        }
    return render(request, 'attractions/favorites.html', context)