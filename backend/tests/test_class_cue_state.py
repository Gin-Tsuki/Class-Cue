"""Regression coverage for Class Cue state API persistence and validation."""
import os
import requests
import pytest

BASE_URL = os.environ["CLASS_CUE_BASE_URL"].rstrip("/")


@pytest.fixture
def client():
    with requests.Session() as session:
        session.headers.update({"Content-Type": "application/json"})
        yield session


def test_get_state_returns_expected_shape(client):
    response = client.get(f"{BASE_URL}/api/state", timeout=15)
    assert response.status_code == 200
    data = response.json()
    for key in ("subjects", "students", "sessions", "lessons", "attendance", "assignments", "grades", "notes"):
        assert key in data
        assert isinstance(data[key], list)


def test_state_round_trip_persists(client):
    original = client.get(f"{BASE_URL}/api/state", timeout=15)
    assert original.status_code == 200
    state = original.json()
    marker = "TEST_round_trip"
    state["notes"] = state["notes"] + [{"id": marker, "studentId": "stu-1", "note": marker, "date": "2026-06-16"}]
    saved = client.put(f"{BASE_URL}/api/state", json=state, timeout=15)
    assert saved.status_code == 200
    assert any(n.get("id") == marker for n in saved.json()["notes"])
    fetched = client.get(f"{BASE_URL}/api/state", timeout=15)
    assert any(n.get("id") == marker for n in fetched.json()["notes"])
    state["notes"] = [n for n in state["notes"] if n.get("id") != marker]
    cleanup = client.put(f"{BASE_URL}/api/state", json=state, timeout=15)
    assert cleanup.status_code == 200


def test_state_rejects_wrong_field_type(client):
    response = client.put(f"{BASE_URL}/api/state", json={"students": "not-a-list"}, timeout=15)
    assert response.status_code == 422