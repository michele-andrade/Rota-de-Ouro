from dataclasses import field
from rest_framework import serializers
from api_rotadeouro import models

class TouristplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Touristplace 
        fields= ('id',
        'name',
        'description',
        'time',
        'payment',
        'adress',
        'latitude',
        'longitude',
        'accessibility')