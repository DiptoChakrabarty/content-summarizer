from django import forms
#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from .models import Profile




class PDFForm(forms.Form):
    myfile = forms.FileField()
    class Meta:
        model=Profile
        fields=['myfile']

class keyForm(forms.Form):
    class Meta:
        model=Profile
        fields=['keys']