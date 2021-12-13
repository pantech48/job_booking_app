from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import WorkingPlace, Booking
from job_booking.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from job_booking.booking_functions.working_place_status import check_status


class WorkingPlaceCreateView(generics.CreateAPIView):
    serializer_class = WorkingPlaceSerializer


class WorkingPlaceListView(generics.ListAPIView):
    serializer_class = WorkingPlaceListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('datetime_from', 'datetime_to',)
    queryset = Booking.objects.all()

class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer

class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('working_place',)
    queryset = Booking.objects.all()