from django.contrib import admin
from .models import EventModel, GuestModel

admin.site.register(EventModel)
admin.site.register(GuestModel)
