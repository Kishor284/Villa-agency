from . models import signup1, sdata, image1
from django import forms

class signforms(forms.ModelForm):
    class Meta:
        model = signup1
        fields ='__all__'


class Leaveform(forms.ModelForm):
    class Meta:
        model=sdata
        fields=['t1','t2','t3','t4','t5','t6']

class imageform(forms.ModelForm):
    class Meta:
        model=image1
        fields= ['name','uimage']
