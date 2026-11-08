from django import forms
from journal.models import Workout, WorkoutSet


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["label", "date"]
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}


class SetForm(forms.ModelForm):
    class Meta:
        model = WorkoutSet
        fields = ["exercise", "load_lb", "reps"]
        labels = {"load_lb": "Weight in pounds"}
