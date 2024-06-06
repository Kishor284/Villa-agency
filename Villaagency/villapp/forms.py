from . models import signup1, sdata, villaimage, Data
from django import forms

class signforms(forms.ModelForm):
    class Meta:
        model = signup1
        fields ='__all__'


class Leaveform(forms.ModelForm):
    class Meta:
        model=sdata
        fields=['t1','t2','t3','t4','t5','t6']



class villaimageform(forms.ModelForm):
    class Meta:
        model=villaimage
        fields=['name','images']


class Dataform(forms.ModelForm):
    class Meta:
        model=Data
        fields=['BED','BATH','ARE','FLO','PAR','IMG']