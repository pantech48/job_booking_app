from django.contrib import admin
from .models import WorkingPlace, Booking

# Register your models here.

class WorkingPlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id',)
    

admin.site.register(WorkingPlace, WorkingPlaceAdmin)
admin.site.register(Booking)