from django.contrib import admin
from .models import Profile  # Use a relative import to import the model

admin.site.register(Profile)
