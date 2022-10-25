from django.shortcuts import render


def home(request):
    return render(request, 'attractions/home.html')

def nearby(request):
    x = 1
    y = 2
    posi = [x,y]

    context = {
        'posi': posi
    }
    return render(request, 'attractions/nearby.html', context)

def found(request):
    fav_attractions = ['a','b','c']

    context = {
        'fav_attractions': fav_attractions
    }
    return render(request, 'attractions/found.html', context)

def favorites(request):
    fav_attractions = ['a','b','c']

    context = {
        'fav_attractions': fav_attractions
    }
    return render(request, 'attractions/favorites.html', context)
