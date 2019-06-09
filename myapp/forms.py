from django import forms
from .models import MyTable

class MyTableForm(forms.ModelForm):
    class Meta():
        model = MyTable
        fields = (
        'name',
        'roll',
        'email',
        )
