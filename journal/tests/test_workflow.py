import pytest
from django.contrib.auth.models import User
from django.test import Client


@pytest.mark.django_db
def test_workout_form_persists_and_is_private():
    from journal.models import Workout, WorkoutSet
    user = User.objects.create_user(username="lifter", password="course-password")
    other = User.objects.create_user(username="other", password="course-password")
    client = Client()
    assert client.get("/").status_code == 302
    client.force_login(user)
    response = client.post("/", {"label": "Leg day", "date": "2026-11-08"})
    workout = Workout.objects.get(owner=user)
    assert response.status_code == 302
    url = f"/workouts/{workout.pk}/"
    assert client.post(url, {"exercise": "Leg press", "load_lb": "100", "reps": "10"}).status_code == 302
    assert WorkoutSet.objects.get(workout=workout).reps == 10
    assert b"Leg press" in client.get(url).content
    invalid = client.post(url, {"exercise": "Leg press", "load_lb": "-1", "reps": "0"})
    assert invalid.status_code == 200
    assert WorkoutSet.objects.count() == 1
    client.force_login(other)
    assert client.get(url).status_code == 404
    assert b"Leg day" not in client.get("/").content


@pytest.mark.django_db
def test_csrf_and_login_pages():
    client = Client(enforce_csrf_checks=True)
    assert client.get("/login/").status_code == 200
    assert client.get("/register/").status_code == 200
    assert client.post("/register/", {}).status_code == 403
