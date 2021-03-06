from django import forms
from .models import Exercise
#DataFlair
class ExerciseCreate(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['id','name','exFile','details','deadline']