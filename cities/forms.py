from cities.models import City

from django import forms


class CityForm(forms.ModelForm):
    name = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'Input the name of the city'}))

    class Meta:
        model = City
        fields = ['name']
