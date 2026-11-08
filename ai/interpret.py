import json
import re

HYPOTHETICAL = re.compile(
    r"^(what if|maybe|should i|hypothetically|suppose|i might)\b",
    re.IGNORECASE,
)
START = re.compile(
    r"^(it is|it's|its|i'm doing|im doing)\s+(.+?)\s+today[.!]?\s*$",
    re.IGNORECASE,
)
LOAD_REPS = re.compile(
    r"(\d+(?:\.\d+)?)\s*(?:lb|lbs|pounds)?\s*(?:x|×|for)\s*(\d+)",
    re.IGNORECASE,
)


def interpret_note(payload: dict) -> dict:
    note = _clean(payload.get("note", ""))
    revision = payload.get("contextRevision") or "none"
    workout = payload.get("workout")
    exercises = payload.get("exercises") or []
    if HYPOTHETICAL.match(note):
        return _clarify(revision, "That sounds like a possibility, not a completed set. Log it manually if you did it.", "intent")
    start = START.match(note)
    if start:
        label = _title(start.group(2))
        if workout and workout.get("id") and not workout.get("ended"):
            if _norm(workout.get("label")) == _norm(label):
                return _proposal(revision, {"kind": "resume_workout", "workoutId": workout["id"], "label": label})
            return _clarify(
                revision,
                f"A {workout.get('label') or 'workout'} is already open. Finish it before starting {label}.",
                "workout",
            )
        return _proposal(revision, {"kind": "start_workout", "label": label})
    matches = _matching_exercises(note, exercises)
    if len(matches) == 0:
        return _clarify(revision, "Which exercise did you mean?", "exercise")
    if len(matches) > 1:
        names = ", ".join(item["name"] for item in matches)
        return _clarify(revision, f"Which exercise did you mean? {names}", "exercise")
    parsed = LOAD_REPS.search(note)
    if not parsed:
        return _clarify(revision, "What weight and how many reps?", "reps")
    exercise = matches[0]
    if not workout or not workout.get("id") or workout.get("ended"):
        return _clarify(revision, "Start a workout before logging a set.", "workout")
    return _proposal(
        revision,
        {
            "kind": "log_set",
            "workoutId": workout["id"],
            "exerciseId": exercise["id"],
            "exerciseName": exercise["name"],
            "loadLb": _pounds(parsed.group(1)),
            "reps": int(parsed.group(2)),
            "assisted": False,
        },
    )


def parse_model_content(content: str) -> dict:
    data = json.loads(content)
    if data.get("status") not in ("proposal", "clarify") or data.get("version") != 1:
        raise ValueError("model response is not a chat proposal")
    proposal = data.get("proposal")
    if isinstance(proposal, dict) and "kind" not in proposal:
        actions = proposal.get("actions")
        if isinstance(actions, list) and actions and isinstance(actions[0], dict) and actions[0].get("kind"):
            data = {**data, "proposal": actions[0]}
    return data


def _proposal(revision: str, proposal: dict) -> dict:
    return {"version": 1, "status": "proposal", "contextRevision": revision, "proposal": proposal}


def _clarify(revision: str, question: str, reason: str) -> dict:
    return {
        "version": 1,
        "status": "clarify",
        "contextRevision": revision,
        "question": question,
        "reason": reason,
    }


def _matching_exercises(note: str, exercises: list) -> list:
    folded = _norm(note)
    head = _norm(LOAD_REPS.sub(" ", folded))
    found = []
    for exercise in exercises:
        name = _norm(exercise.get("name", ""))
        if len(name) < 3:
            continue
        if name in folded or (len(head) >= 3 and head in name):
            found.append(exercise)
    return [item for item in found if not _contained(item, found)]


def _contained(item, found) -> bool:
    name = _norm(item["name"])
    return any(name != _norm(other["name"]) and name in _norm(other["name"]) for other in found)


def _pounds(value: str) -> str:
    if "." in value:
        whole, frac = value.split(".", 1)
        frac = (frac + "00")[:2].rstrip("0")
        return whole if not frac else f"{whole}.{frac}"
    return value


def _title(value: str) -> str:
    return " ".join(part.capitalize() for part in value.split())


def _clean(value: str) -> str:
    return " ".join(str(value).replace("’", "'").split())


def _norm(value) -> str:
    return " ".join(str(value or "").replace("’", "'").lower().split())
