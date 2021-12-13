from .models import WorkingPlace
from rest_framework import viewsets, permissions
from .serializers import WorkingPlaceSerializer


class WorkingPlaceViewSet(viewsets.ModelViewSet):
    queryset = WorkingPlace.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = WorkingPlaceSerializer