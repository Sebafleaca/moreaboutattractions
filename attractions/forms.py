from django import forms

class LocationForm(forms.Form):
    coordinates = forms.CharField(max_length=200)