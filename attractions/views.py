from django.shortcuts import render


def home(request):
    variable = 1

    context = {
        'variable': variable
    }
    return render(request, 'attractions/home.html', context)