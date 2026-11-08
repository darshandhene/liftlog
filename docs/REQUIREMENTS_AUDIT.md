# Assignment requirements audit

Checked November 8, 2026 against the supplied P2 - A3 & A4 assignment. This is a readiness assessment, not a promised grade. A3 and A4 have separate rubrics.

## P2-A3 first draft

| Criterion | Points | Assessment and evidence |
|---|---:|---|
| Updated Product Scope | 15 | Covered by `PRODUCT_SCOPE.md`: idea, problem, users, three planned features, scope refinement and differentiation. Comparison with the original P2-A2 submission needs the student's confirmation; that submission was not supplied for this audit. |
| Functional Django Foundation | 40 | Covered: Django project and journal app; Workout and WorkoutSet with a foreign-key relationship and migration; working views, inherited templates, validated forms, account-owned database workflow. Automated checks verify persisted visible results and account isolation. |
| Initial AI Implementation / Technical Plan | 20 | Covered at draft level by `README_AI.md` and the runnable rule-based experiment: proposed extraction technique, inputs/outputs, Django interaction and feasibility evidence. A hosted model has not been selected, and the experiment is not connected to Django; full integration is not required for A3. |
| Development Progress and Roadmap | 15 | Covered by `ROADMAP.md`: all six requested task categories have status, responsible member and completion target. Confirm Darshan's individual ownership against the P2-A2 contribution contract. |
| GitHub Organization and Reproducibility | 10 | Required code, migration, dependencies, ignore rules, README and AI documentation are present. Setup and database workflow checks pass. Remote publishing is performed after this audit; instructor access must be maintained and the repository URL still needs Canvas submission. |

Overall: the inspected implementation appears ready for the A3 milestone, subject to the original proposal/contribution checks and submission steps above. Markdown scope length is approximately one page; no separate formatted one-page attachment was supplied or verified.

## P2-A4 final project

| Part | Points | Current status / remaining requirements |
|---|---:|---|
| 1. Product scope and UX | 10 | Scope, differentiation and manual workflow exist. Three planned features are documented, but conversational entry and trends are not implemented. Complete and assess the three meaningful product features and user experience. |
| 2. Django development | 25 | Models, relationship, migrations, create/read operations, templates, URLs, forms, authentication and ownership checks exist. Add update/delete where relevant, a meaningful JSON or external API, and a data-oriented feature. |
| 3. AI integration | 25 | Initial technical plan and deterministic experiment only. Select and justify the actual model, integrate it into Django and user data, validate output and implement graceful model/provider failure handling. The standalone experiment does not satisfy final integration requirements. |
| 4. Evaluation and improvement | 15 | Five automated tests pass, but these do not constitute the required five-row realistic evaluation table. Define metrics, record actual outputs, quality scores and measured latency, document two genuine failures/limitations, and show a tested before/modification/after improvement. |
| 5. Deployment and production | 15 | Local prototype only. Deploy the primary workflow or supply an applicable technical justification for local deployment. Document resources, compare two realistic deployment approaches and costs, analyze 10,000 daily users with assumptions, and address production security, rate limiting, monitoring and privacy. Current default debug/localhost configuration is for development. |
| 6. Documentation and reproducibility | 10 | Required source/setup/AI documents are present for the draft. Update them with the final model, features, deployment and actual evaluation evidence. Maintain credential protection and reproducibility. |

A4 also requires a product demonstration video of no more than three minutes, showing the actual application, AI workflow, limitations and next steps. No video is present. P1 independence and team contribution compliance cannot be verified from this standalone folder.

## Verification performed

- Existing environment: `python -m pytest -q`: **5 passed in 0.50 seconds**.
- `python manage.py check`: **no issues**.
- `python manage.py makemigrations --check --dry-run`: **no changes detected**.
- `python -m pip check`: **no broken requirements**.
- Temporary empty SQLite database: migrations, real registration, workout and set creation, visible result, logout, login and persisted result all passed using Django's test client. The temporary database was removed. This checks application behavior, not visual browser layout or a fresh dependency installation.
- Existing tests cover validation, account isolation, CSRF and three interpreter examples. No hosted model was called.
- Common credential-pattern scan over files eligible for commit found no matches; no claim of an exhaustive secret audit is made.

## Git ignore audit

Ignored as intended: `.venv/`, `venv/`, `.env`, `.env.*`, private-key file extensions, SQLite/database files, bytecode, Python/pytest caches, `.DS_Store` and `.bin`/`.pt`/`.safetensors` model weights. `.env.example` is explicitly allowed.

Required Python code, templates, migrations, `requirements.txt`, `.gitignore`, `README.md`, `README_AI.md` and supporting scope/roadmap documents are eligible for commit. No required submission files were found accidentally ignored. The local database and installed environment are reproducible generated files, not submission requirements.
