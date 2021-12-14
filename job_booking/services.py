from django_filters import rest_framework as filters 
from .models import *


class WorkingPlaceFilter(filters.FilterSet):
    datetime_from = filters.DateTimeFilter(lookup_expr="lt")
    datetime_to = filters.DateTimeFilter(lookup_expr="lt")

    class Meta:
        model = Booking
        fields = [
            'datetime_from',
            'datetime_to',
        ]