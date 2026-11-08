from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Workout(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="web_workouts")
    label = models.CharField(max_length=80)
    date = models.DateField(default=timezone.localdate)

    class Meta:
        ordering = ["-date", "-pk"]


class WorkoutSet(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="sets")
    exercise = models.CharField(max_length=120)
    load_lb = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])
    reps = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])

    class Meta:
        ordering = ["pk"]
