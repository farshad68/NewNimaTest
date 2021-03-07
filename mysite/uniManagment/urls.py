from django.conf.urls import url
from django.urls import path
from uniManagment.views import dashboard

from uniManagment.views import exercise
from uniManagment.views import exerciseIndex
from uniManagment.views import exerciseUpload

from uniManagment.views import sendExercise
from uniManagment.views import submitedExerciseIndex

from uniManagment.views import downloadExerciseFiles
from uniManagment.views import downloadSubmitedExerciseFiles

from django.conf.urls import include

urlpatterns = [
	url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^exercise/index", exerciseIndex, name="exerciseIndex"),
    url(r"^exercise/exerciseUpload", exerciseUpload, name="exerciseUpload"),
    url(r"^exercise/", exercise, name="exercise"),
    url(r"^submitedexercise/index", submitedExerciseIndex, name="submitedExerciseIndex"),
	path("submitedexercise/sendExercise/<int:ExeId>", sendExercise, name="sendExercise"),
	path("download/exerciseFiles/<str:path>", downloadExerciseFiles, name="downloadExerciseFiles"),
	path("download/submitedExerciseFiles/<str:path>", downloadSubmitedExerciseFiles, name="downloadSubmitedExerciseFiles"),
	url(r"^/", dashboard, name="dashboard"),
	path('', dashboard, name="dashboard"),
]
