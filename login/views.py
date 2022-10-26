from os import access
from shutil import ExecError
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Users
from .forms import UserForm


def index(request):
    form_class = UserForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            new_user = Users()
            access_user_name = form.cleaned_data['user_name']
            new_user.user_name = str(access_user_name)
            new_user.save()
            return HttpResponseRedirect('/')
    else:
        form = UserForm()

    rendered_form = form.render("login/form_snippet.html")
    return render(request, 'login/index.html', {'form': rendered_form})    

    
def user_view(request):
    usr_name = Users.objects.get(user_name='user001')
    #old_user = get_object_or_404(Users, user_name=usr_name)
    
    print_all = Users.objects.all()

    context = { 'old_user' : str(usr_name),
                'print_all': print_all,
                }

    return render(request, 'login/user.html', context)