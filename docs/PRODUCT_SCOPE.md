# Liftlog updated product scope

P2-A3 first draft · Darshan · November 8, 2026

Liftlog is a strength-training journal for recreational lifters who need a quick way to record workouts and understand their history. It addresses the friction of logging sets during a session and recovering useful information from scattered notes.

The target users are students and other recreational strength trainees who want a straightforward record of exercises, weights, repetitions, and sessions. The intended value is simple logging and useful history, with conversational entry that users can inspect before saving.

## Three planned core features

1. Workout logging and history. Create sessions, record completed sets, and review history. The submitted Django draft implements this workflow using account-owned Workout and WorkoutSet models.
2. Conversational workout entry. Interpret a casual note into a structured proposal grounded in a workout and exercise catalog. A rule-based experiment is included; hosted model selection and browser integration remain planned.
3. Training trends. Summarize recorded volume and workout frequency using Django queries and a JSON API. This feature is planned for the final submission and is not implemented in this standalone draft.

## Scope refinement

The broader Liftlog concept includes an offline-first mobile experience. This course submission focuses on a standalone Django browser journal to demonstrate the required views, templates, forms, authentication, model relationships, and database workflow. It starts with an empty database and does not include or depend on the separate mobile implementation.

The final course work will prioritize conversational entry and trends. Nutrition, recovery integrations, crowd reporting, and broader coaching are outside this milestone.

## Differentiation

The intended advantage is low-friction logging with catalog-grounded conversational entry and explicit review before data changes. Manual entry remains available when AI is unavailable. This is a proposed advantage to evaluate, not a claim that competitors lack these capabilities.
