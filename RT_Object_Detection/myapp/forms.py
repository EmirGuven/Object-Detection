from django.forms import ModelForm, widgets
from .models import *

class Object_DataForm(ModelForm):
    class Meta:
        model = Object_Data
        fields = ['Object_Id', 'Name']