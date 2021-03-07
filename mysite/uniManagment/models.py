from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	studentNumber = models.TextField(max_length=15, blank=True)
	isStudent = models.BooleanField()

class Video(models.Model):
	id = models.AutoField(primary_key=True)
	createBy = models.ForeignKey(Profile, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	vidFile = models.FileField(upload_to='videos/')
	details = models.CharField(max_length=300)
	deadline = models.DateTimeField(editable=True)

	def __str__(self):
		return self.name

class Exercise(models.Model):
	id = models.AutoField(primary_key=True)
	createBy = models.ForeignKey(Profile, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	exFile = models.FileField(upload_to='exerciseFiles/')
	details = models.CharField(max_length=300)
	deadline = models.DateTimeField(editable=True)

	def __str__(self):
		return self.name

class SubmitedExercise(models.Model):
	id = models.AutoField(primary_key=True)
	submitBy = models.ForeignKey(Profile, on_delete=models.CASCADE)
	exe = models.ForeignKey(Exercise, on_delete=models.CASCADE)
	score = models.DecimalField(decimal_places=2,max_digits=4,null=True,blank=True)
	file = models.FileField(upload_to='submitedExerciseFiles/')
	details = models.CharField(max_length=300)
		
	def __str__(self):
		return self.details

