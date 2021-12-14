from django_filters import rest_framework as filters 
from .models import *


class WorkingPlaceFilter(filters.FilterSet):
    datetime_from = filters.DateTimeFilter(field_name='datetime_from', lookup_expr="lt")
    datetime_to = filters.DateTimeFilter(field_name='datetime_to', lookup_expr="gt")

    class Meta:
        model = Booking
        fields = [
            'datetime_from',
            'datetime_to',
        ]