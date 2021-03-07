from django import forms
from .models import Exercise
from .models import SubmitedExercise
#DataFlair
class ExerciseCreate(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['id','name','exFile','details','deadline']
class SubmitExerciseCreate(forms.ModelForm):
    class Meta:
        model = SubmitedExercise
        fields = ['id','file','details']