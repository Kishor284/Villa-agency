from . models import signup1
from django import forms

class signforms(forms.ModelForm):
    class Meta:
        model = signup1
        fields ='__all__'
