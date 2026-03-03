import pytest
from datetime import datetime
from pydantic import ValidationError
from app.models import Prompt, PromptCreate, PromptUpdate, Collection, PromptList, CollectionList

# ============== Tests for Prompt Models ==============

def test_prompt_create():
    data = {
      "title": "Prompt Title",
      "content": "Some content",
    }
    prompt = PromptCreate(**data)
    assert prompt.title == "Prompt Title"
    assert prompt.content == "Some content"


def test_prompt_invalid_creation():
    data = {
      "title": "",
      "content": "",
    }
    with pytest.raises(ValidationError):
        PromptCreate(**data)


def test_prompt_update():
    data = {
      "title": "Updated Title",
    }
    prompt_update = PromptUpdate(**data)
    assert prompt_update.title == "Updated Title"


def test_prompt_model_defaults():
    prompt = Prompt(title="Title", content="Content", created_at=datetime.now(), updated_at=datetime.now())
    assert prompt.id is not None
    assert isinstance(prompt.created_at, datetime)
    assert isinstance(prompt.updated_at, datetime)

# ============== Tests for Collection Models ==============

def test_collection_create():
    data = {
      "name": "Collection Name",
    }
    collection = Collection(**data)
    assert collection.name == "Collection Name"


def test_collection_invalid_creation():
    data = {
      "name": "",
    }
    with pytest.raises(ValidationError):
        Collection(**data)


def test_collection_model_defaults():
    collection = Collection(name="Name", created_at=datetime.now())
    assert collection.id is not None
    assert isinstance(collection.created_at, datetime)

# ============== Tests for List Models ==============

def test_prompt_list_serialization():
    prompt = Prompt(id="1", title="Title", content="Content", created_at=datetime.now(), updated_at=datetime.now())
    prompt_list = PromptList(prompts=[prompt], total=1)
    serialized_data = prompt_list.json()
    assert "Title" in serialized_data


def test_collection_list_serialization():
    collection = Collection(id="1", name="Name", created_at=datetime.now())
    collection_list = CollectionList(collections=[collection], total=1)
    serialized_data = collection_list.json()
    assert "Name" in serialized_data
