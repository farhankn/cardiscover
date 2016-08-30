import models
import serializers
from rest_framework import viewsets, permissions


class carNameViewSet(viewsets.ModelViewSet):
    """ViewSet for the carName class"""

    queryset = models.carName.objects.all()
    serializer_class = serializers.carNameSerializer
    permission_classes = [permissions.IsAuthenticated]


class ManufacturerViewSet(viewsets.ModelViewSet):
    """ViewSet for the Manufacturer class"""

    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated]


