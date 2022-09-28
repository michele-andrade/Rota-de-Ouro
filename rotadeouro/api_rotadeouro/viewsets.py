from rest_framework import viewsets
from api_rotadeouro import models
from api_rotadeouro import serializers

class TouristplaceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TouristplaceSerializer
    queryset = models.Touristplace.objects.all()