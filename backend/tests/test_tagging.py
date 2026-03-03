import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    from main import app  # Import the FastAPI app
    return TestClient(app)


def test_get_all_tags(client):
    # Test retrieving all tags (should initially be empty)
    response = client.get("/tags")
    assert response.status_code == 200
    assert response.json() == []


def test_add_tags_to_prompt(client, sample_prompt_data):
    # Create a prompt first
    prompt_response = client.post("/prompts", json=sample_prompt_data)
    prompt_id = prompt_response.json()["id"]

    # Add tags to the created prompt
    tags_data = {"tags": ["urgent", "draft"]}
    response = client.post(f"/prompts/{prompt_id}/tags", json=tags_data)

    assert response.status_code == 200
    updated_prompt = response.json()
    assert set(updated_prompt["tags"]) == {"urgent", "draft"}


def test_remove_tags_from_prompt(client, sample_prompt_data):
    # Create a prompt first
    prompt_response = client.post("/prompts", json=sample_prompt_data)
    prompt_id = prompt_response.json()["id"]

    # Add tags to the created prompt
    tags_data = {"tags": ["urgent", "draft"]}
    client.post(f"/prompts/{prompt_id}/tags", json=tags_data)

    # Remove a tag from the prompt
    tags_to_remove = {"tags": ["urgent"]}
    response = client.delete(f"/prompts/{prompt_id}/tags", json=tags_to_remove)

    assert response.status_code == 200
    updated_prompt = response.json()
    assert set(updated_prompt["tags"]) == {"draft"}


def test_filter_prompts_by_tags(client, sample_prompt_data):
    # Setup: create multiple prompts with different tags
    prompt1_data = {**sample_prompt_data, "title": "Prompt 1"}
    prompt2_data = {**sample_prompt_data, "title": "Prompt 2"}

    response1 = client.post("/prompts", json=prompt1_data)
    prompt1_id = response1.json()["id"]
    response2 = client.post("/prompts", json=prompt2_data)
    prompt2_id = response2.json()["id"]

    # Add tags to the prompts
    client.post(f"/prompts/{prompt1_id}/tags", json={"tags": ["tag1", "tag2"]})
    client.post(f"/prompts/{prompt2_id}/tags", json={"tags": ["tag2"]})

    # Filter prompts by tag "tag1"
    response = client.get("/prompts?tags=tag1")

    assert response.status_code == 200
    filtered_prompts = response.json()["prompts"]

    # Only prompt1 should have "tag1"
    assert len(filtered_prompts) == 1
    assert filtered_prompts[0]["id"] == prompt1_id
