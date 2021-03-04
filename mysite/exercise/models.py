from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exercise(models.Model):
	createBy = models.ForeignKey(User)
	name = models.CharField(max_length=30)
	exFile = models.CharField(max_length=200)
	details = models.CharField(max_length=300)
	deadline = models.DateTimeField(editable=False)