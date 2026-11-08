# Liftlog Assignment 3

Liftlog helps recreational strength trainees record completed workouts and review their history. This is a standalone P2-A3 first draft for INFO 490. It contains the Django course prototype and the documentation required for the November 9, 2026 milestone.

## Features included

- Register, sign in, and sign out using Django authentication.
- Create a workout and save exercise sets with weights and repetitions.
- View saved workouts and sets; each account can access only its own journal.
- Validate forms and protect submissions using CSRF tokens.
- Run an initial rule-based experiment for conversational workout entry.

`journal.Workout` belongs to a Django user. `journal.WorkoutSet` belongs to a Workout through a foreign key. Migrations are included. The AI experiment does not write database records and is not integrated into the browser UI yet; a working AI integration is planned for the final project.

## Install and run

Requires Python 3.11 or newer. These commands work on macOS and Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py runserver 127.0.0.1:8000
```

On Windows, use `py -m venv .venv`, then `.venv\Scripts\python` in place of `.venv/bin/python`.

Open http://127.0.0.1:8000/register/ and create an account. Create a workout, add a set such as Leg press / 100 pounds / 10 reps, and save. Reload the page to see the saved record. The Workouts link returns to history. Sign out and create another account to check that the first account's records are private.

No API key, account seed, existing database, or environment file is needed. Migrations create a new empty SQLite database. Choose your own local test credentials; no credentials are shipped.

## Configuration

Settings read process environment variables directly; `.env` files are not loaded. `DJANGO_SECRET_KEY` is optional for a local demo: an ephemeral development key is generated at startup if absent, so sessions expire when the process restarts. Set a persistent strong key through the environment to keep sessions across restarts. `DJANGO_DEBUG` defaults to `1` for local development. Public deployment is not part of this first draft; production requires appropriate host, HTTPS, cookie, secret, logging, and abuse-control configuration.

## Verify

```bash
.venv/bin/python -m pytest -q
.venv/bin/python manage.py check
.venv/bin/python manage.py makemigrations --check --dry-run
```

See [AI plan](README_AI.md), [one-page product scope](docs/PRODUCT_SCOPE.md), [roadmap](docs/ROADMAP.md), and [verification](docs/VERIFICATION.md).

## Assignment submission

Review product changes against your P2-A2 submission and confirm individual/team ownership. Push this folder to its own instructor-accessible GitHub repository, then submit its repository URL in Canvas by November 9, 2026 at 11:59 PM. Only this folder is intended for submission. It has no dependency on the separate full product repository.

This first draft excludes the private mobile application, synchronization implementation, hosted AI adapters, keys, personal databases, Git history, and internal design documents. A three-minute demonstration video and complete final requirements are due with P2-A4 on December 8.
