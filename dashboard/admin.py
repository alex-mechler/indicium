from django.contrib import admin
from .models import Symptoms, User


# Uncomment the lines below to use web admin interface on the database

admin.site.register(Symptoms)
admin.site.register(User)
