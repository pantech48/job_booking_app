from django.contrib import admin
from django.urls import path, include
from job_booking.views import *

app_name = 'job_booking'
urlpatterns = [
    path('working_place/create/', WorkingPlaceCreateView.as_view()),
    path('working_place/list/', WorkingPlaceListView.as_view()),
    path('working_place/book/', BookingCreateView.as_view()),
    path('booking/list/', BookingListView.as_view())
]