from copy import deepcopy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_dict


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Snapshot the in-memory activities and restore after each test to keep tests isolated."""
    original = deepcopy(activities_dict)
    yield
    activities_dict.clear()
    activities_dict.update(deepcopy(original))
