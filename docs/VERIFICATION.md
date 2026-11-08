# Standalone submission verification

Recorded November 8, 2026 in the standalone Liftlog Assignment 3 folder, using a newly created virtual environment installed from its requirements.txt.

| Check | Actual result |
|---|---|
| `.venv/bin/python -m pytest -q` | 5 tests passed in 0.48 seconds |
| `.venv/bin/python manage.py check` | No issues |
| `.venv/bin/python manage.py makemigrations --check --dry-run` | No changes detected |
| `.venv/bin/python manage.py migrate` | All migrations applied to a new empty database |

The workflow test checks authentication, workout and set persistence, visible saved results, invalid numerical input, and account isolation. The CSRF test checks login/registration pages and rejection of a form POST without a token. Three rule-based interpreter tests check extraction, missing information, and hypothetical input.

No external AI provider was called. No live-model quality, production deployment, or GitHub/Canvas submission is claimed. The standalone project contains no mobile code or dependencies on the original project. Local verification created an ignored `.venv` and empty SQLite database; neither is part of the upload ZIP or Git submission files.
