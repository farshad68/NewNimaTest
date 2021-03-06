from django.shortcuts import render , redirect

from .models import Exercise
from .models import Profile
from .models import SubmitedExercise

from .forms import ExerciseCreate

from django.http import HttpResponse

import os

from django.conf import settings

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
			uu = request.user;
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


	args = {}
	args['SubmitedExercise']=submitedExercise;
	args['exercises']=exercises;
	return render(request, 'submitedExercise/index.html', args)

def sendExercise(request,id):
	args={}
	args['id']=id
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

def whatIsRole(input):
	role = ''
	for g in input:
		print(g.name)
		if(g.name == 'student'):
			role = 'student'
		
		if(g.name == 'ostad'):
			role = 'master'
	return role
