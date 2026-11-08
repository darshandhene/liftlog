from ai.interpret import interpret_note


def payload(note):
    return {"note": note, "contextRevision": "demo:1",
            "workout": {"id": "demo", "label": "Leg Day", "ended": False},
            "exercises": [{"id": "leg-press", "name": "Leg Press", "type": "machine"}]}


def test_completed_set_uses_catalog_id():
    result = interpret_note(payload("Leg press 100 x 10"))
    assert result["proposal"]["exerciseId"] == "leg-press"
    assert result["proposal"]["loadLb"] == "100"
    assert result["proposal"]["reps"] == 10


def test_missing_repetitions_asks_for_clarification():
    assert interpret_note(payload("Leg press 100"))["reason"] == "reps"


def test_hypothetical_input_does_not_log_a_set():
    assert interpret_note(payload("What if I leg press 100 x 10"))["reason"] == "intent"
