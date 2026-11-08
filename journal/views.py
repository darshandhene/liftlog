from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from journal.forms import SetForm, WorkoutForm
from journal.models import Workout


def register(request):
    form = UserCreationForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        login(request, form.save())
        return redirect("journal-home")
    return render(request, "journal/form.html", {"form": form, "title": "Create account"})


@login_required
def home(request):
    form = WorkoutForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        workout = form.save(commit=False)
        workout.owner = request.user
        workout.save()
        return redirect("journal-detail", pk=workout.pk)
    return render(request, "journal/home.html", {"form": form, "workouts": Workout.objects.filter(owner=request.user)})


@login_required
def detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk, owner=request.user)
    form = SetForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        entry = form.save(commit=False)
        entry.workout = workout
        entry.save()
        return redirect("journal-detail", pk=workout.pk)
    return render(request, "journal/detail.html", {"form": form, "workout": workout})
