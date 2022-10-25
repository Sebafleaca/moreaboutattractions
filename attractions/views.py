from django.shortcuts import render

from . import googleapi


def home(request):
    return render(request, 'attractions/home.html')

def nearby(request):
    if request.method == 'POST':
        actual_location = str(request.POST.get('actual_location',))
        googleapi.GoogleApi.set_location(actual_location)
    return render(request, 'attractions/nearby.html')

def found(request):
    google_response = googleapi.GoogleApi().result
    context = {
        'status': google_response['status'],
        'message': google_response['error_message']
    }
    return render(request, 'attractions/found.html', context)

def favorites(request):
    fav_attractions = ['a','b','c']

    context = {
        'fav_attractions': fav_attractions
    }
    return render(request, 'attractions/favorites.html', context)
