import models

from rest_framework import serializers


class carNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.carName
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'Manufacturer', 
            'Price', 
            'mileage', 
            'engine', 
            'power', 
            'description', 
            'cardheko', 
            'cartrade', 
            'youtubeurl', 
            'imageUrl', 
        )


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Manufacturer
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


