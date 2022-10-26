from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .models import Users
from .forms import UserForm


def index(request):
    
    form = UserForm(request.POST or None)
    rendered_form = form.render("login/form_snippet.html")

    if form.is_valid():
        utente = form.cleaned_data['user_name']
        get_user = Users.objects.filter(user_name=utente)
        if get_user:
            new_user = get_user
        else:
            new_user = Users.objects.create()
            new_user.user_name = utente
            new_user.save()

    context = {'form': rendered_form}

    HttpResponseRedirect('/thanks/')
    
    return render(request, 'login/index.html', context)


def user_view(request):
    usr_name = 'pino'
    old_user = get_object_or_404(Users, user_name=usr_name)
    
    print_all = Users.objects.all()

    context = { 'old_user' : old_user,
                'print_all': print_all,}

    return render(request, 'login/user.html', context)