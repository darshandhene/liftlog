# Liftlog initial AI technical plan

## Proposed feature

Conversational workout entry will turn a lifter's note into a structured proposal, grounded in the open workout and an exercise catalog. The user will review it before any database change. A language model is proposed for structured information extraction, not for medical advice or prescribing exercise.

A hosted instruction-following model supporting JSON output is the initial architecture choice. It avoids a GPU on the Django host, but introduces provider costs, latency, network dependence, and privacy requirements. The final provider and model are not selected for this standalone submission; selection will compare extraction accuracy, clarification behavior, malformed-output rate, latency, and cost on realistic notes.

## Input and output

Input: note `Leg press 100 x 10`, an open workout, catalog entries with stable identifiers, and a context revision. Expected output: a proposal containing exercise id `leg-press`, load `100` pounds, and 10 repetitions. Missing repetitions should trigger a clarification question. Hypothetical or ambiguous notes should not silently create records.

## Initial experimentation included

`ai/interpret.py` contains a deterministic rule-based experiment extracted from the broader Liftlog work. It is not a language model, and its tests do not establish model accuracy. Run:

```bash
.venv/bin/python -m pytest ai/test_interpret.py -q
```

The three included cases exercise completed-set extraction, missing-repetition clarification, and rejection of hypothetical input. The experiment uses synthetic workout/catalog data, calls no external service, requires no credentials, and does not modify journal records.

## Planned Django interaction

Browser note and explicit consent → authenticated Django view → query the user's workout and catalog → minimize and prepare model input → hosted model → validate response schema and catalog identifiers → show editable proposal → explicit confirmation → save WorkoutSet → visible result.

The first draft browser currently supports manual entry. The AI experiment has not been connected to browser forms or the database. This plan and runnable experiment demonstrate initial feasibility for A3; final integrated AI remains on the roadmap.

## Reliability and privacy work

Reject invalid weights and repetitions, unknown exercise ids, stale workouts, and unexpected response shapes before saving. Ask for missing details rather than inventing them. Keep a manual entry path during provider errors or timeouts. Store keys only in server environment variables, minimize submitted text, require consent, and avoid logging personal notes. Evaluate ambiguity, unsupported units, malformed JSON, rate limits, and timeouts before deployment. Five realistic measured tests, two genuine limitations, and an evidence-based improvement are planned for P2-A4.
