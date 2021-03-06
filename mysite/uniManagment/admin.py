from django.contrib import admin

from .models import Exercise
from .models import Profile

admin.site.register(Exercise)
admin.site.register(Profile)
