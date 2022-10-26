from django import forms

class UserForm(forms.Form):
    user_name = forms.CharField(label='User', max_length=200)

