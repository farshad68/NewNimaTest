from django.shortcuts import render , redirect

from .models import Exercise
from .models import Profile
from .models import SubmitedExercise

from .forms import ExerciseCreate
from .forms import SubmitExerciseCreate

from django.http import HttpResponse

import os

from django.conf import settings

from django.shortcuts import get_list_or_404, get_object_or_404

from django.http import Http404

def dashboard(request):
	
	args = {}     
	args['role'] = 	whatIsRole(request.user.groups.all())

	profiles = Profile.objects.all()
	

	uu = request.user;
	for p in profiles :
		if(p.user == uu):
			if(p.isStudent == True):
				args['isStudent'] = True
			else:
				args['isStudent'] = False

	print(profiles)

	return render(request, "users/dashboard.html",args)

def exercise(request):
	args = {}
	args['role'] = 	whatIsRole(request.user.groups.all())
	return render(request, "exercise/exeDashboard.html",args)

def exerciseIndex(request):
	exercises = Exercise.objects.all()
	return render(request, 'exercise/index.html', {'exercises': exercises})

def exerciseUpload(request):
	upload = ExerciseCreate()
	if request.method == 'POST':
		upload = ExerciseCreate(request.POST, request.FILES)
		if upload.is_valid():
			ee = upload.save(commit=False)
			uu = request.user
			profiles = Profile.objects.all()
			for p in profiles :
				if(p.user == uu):
					ee.createBy = p
			ee.save()
			return redirect('exerciseIndex')
		else:
			return HttpResponse("""your form is wrong""")
	else:
		return render(request, 'exercise/upload_form.html', {'upload_form':upload})

def submitedExerciseIndex(request):
	exercises = Exercise.objects.all()
	submitedExercise = SubmitedExercise.objects.all()
	print(exercises)
	print(submitedExercise)
	args = {}
	args['submitedExercise']=submitedExercise;
	args['exercises']=exercises;

	return render(request, 'submitedExercise/index.html', args)

def sendExercise(request,ExeId):
	upload = SubmitExerciseCreate()
	exe = get_object_or_404(Exercise, id=ExeId)
	if request.method == 'POST':
		upload = SubmitExerciseCreate(request.POST, request.FILES)
		if upload.is_valid():
			ee = upload.save(commit=False)
			uu = request.user
			profiles = Profile.objects.all()
			for p in profiles :
				if(p.user == uu):
					ee.submitBy = p
			ee.exe = exe
			ee.score = -1
			ee.save()
			return redirect('submitedExerciseIndex')
		else:
			print(upload.errors)
			return HttpResponse("""your form is wrong""")
	else:
		args={}
		
		args['Id']=id
		args['exe']=exe
		args['upload_form']=upload
		return render(request, 'submitedExercise/sendExercise.html', args)


def downloadExerciseFiles(request, path):
	print(path)
	print(os.path.join(settings.MEDIA_ROOT,"exerciseFiles", path))
	file_path = os.path.join(settings.MEDIA_ROOT,"exerciseFiles", path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404

def downloadSubmitedExerciseFiles(request, path):
	print(path)
	print(os.path.join(settings.MEDIA_ROOT,"submitedExerciseFiles", path))
	file_path = os.path.join(settings.MEDIA_ROOT,"submitedExerciseFiles", path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404

def whatIsRole(input):
	role = ''
	for g in input:
		print(g.name)
		if(g.name == 'student'):
			role = 'student'
		
		if(g.name == 'ostad'):
			role = 'master'
	return role
