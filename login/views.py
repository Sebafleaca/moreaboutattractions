from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Users
from .forms import UserForm


def index(request):
    
    form = UserForm(request.POST or None)
    rendered_form = form.render("login/form_snippet.html")

    if form.is_valid():
        new_user = Users.objects.create()
        new_user.user_name = form.cleaned_data['user_name']
        new_user.save()

    context = {'form': rendered_form}

    HttpResponseRedirect('/thanks/')
    return render(request, 'login/index.html', context)

def user_view(request):

    old_user = Users.objects.all()

    context = { 'old_user' : old_user }

    return render(request, 'login/user.html', context)