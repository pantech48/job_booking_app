from rest_framework import serializers
from .models import WorkingPlace, Booking


class WorkingPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingPlace
        fields = '__all__'


class WorkingPlaceListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Booking
        fields = ('working_place', 'user', )


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Booking
        fields = ('working_place', 'datetime_from', 'datetime_to', 'user',)