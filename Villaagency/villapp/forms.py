from . models import signup
from django import forms

class signforms(forms.ModelForm):
    class Meta:
        model = signup
        fields ='__all__'
