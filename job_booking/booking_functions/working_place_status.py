import datetime
from job_booking.models import WorkingPlace, Booking

def check_status(working_place, datetime_from, datetime_to):
    status_list = []
    booking_list = Booking.objects.filter(working_place=working_place)
    for booking in booking_list:
        if booking.datetime_from > datetime_to or booking.datetime_to < datetime_from:
            status_list.append(True)
        else:
            status_list.append(False)
    return all(status_list)