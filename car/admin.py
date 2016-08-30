from django.contrib import admin
from django import forms
from .models import carName, Manufacturer

class carNameAdminForm(forms.ModelForm):

    class Meta:
        model = carName
        fields = '__all__'


class carNameAdmin(admin.ModelAdmin):
    form = carNameAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'Manufacturer', 'Price', 'mileage', 'engine', 'power', 'description', 'cardheko', 'cartrade', 'youtubeurl', 'imageUrl']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'Manufacturer', 'Price', 'mileage', 'engine', 'power', 'description', 'cardheko', 'cartrade', 'youtubeurl', 'imageUrl']

admin.site.register(carName, carNameAdmin)


class ManufacturerAdminForm(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = '__all__'


class ManufacturerAdmin(admin.ModelAdmin):
    form = ManufacturerAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Manufacturer, ManufacturerAdmin)


