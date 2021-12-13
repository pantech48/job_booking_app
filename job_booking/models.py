from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class WorkingPlace(models.Model):
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return f'{self.id}'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    working_place = models.ForeignKey(WorkingPlace, on_delete=models.CASCADE)
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.working_place} from {self.datetime_from} to {self.datetime_to}'




