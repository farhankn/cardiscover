from django import forms
from .models import carName, Manufacturer


class carNameForm(forms.ModelForm):
    class Meta:
        model = carName
        fields = ['name', 'Manufacturer', 'Price', 'mileage','fueltype','bodytype', 'engine', 'power', 'description', 'cardheko', 'cartrade', 'youtubeurl', 'imageUrl']


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name']


