import pytest
from app.models import Prompt, Collection
from app.storage import Storage
from datetime import datetime

@pytest.fixture
def storage():
    return Storage()

 
# ============== Prompt Operations Tests ==============

def test_create_prompt(storage):
    prompt = Prompt(id="1", title="Test", content="Test content", created_at=datetime.now(), updated_at=datetime.now())
    result = storage.create_prompt(prompt)
    assert result.id == "1"
    assert result.title == "Test"


def test_get_prompt(storage):
    prompt = Prompt(id="1", title="Test", content="Test content", created_at=datetime.now(), updated_at=datetime.now())
    storage.create_prompt(prompt)
    result = storage.get_prompt("1")
    assert result is not None
    assert result.title == "Test"


def test_update_prompt(storage):
    prompt = Prompt(id="1", title="Test", content="Test content", created_at=datetime.now(), updated_at=datetime.now())
    storage.create_prompt(prompt)
    updated_prompt = Prompt(id="1", title="Updated", content="Updated content", created_at=datetime.now(), updated_at=datetime.now())
    result = storage.update_prompt("1", updated_prompt)
    assert result is not None
    assert result.title == "Updated"


def test_delete_prompt(storage):
    prompt = Prompt(id="1", title="Test", content="Test content", created_at=datetime.now(), updated_at=datetime.now())
    storage.create_prompt(prompt)
    result = storage.delete_prompt("1")
    assert result is True


def test_get_all_prompts(storage):
    prompt = Prompt(id="1", title="Test", content="Test content", created_at=datetime.now(), updated_at=datetime.now())
    storage.create_prompt(prompt)
    prompts = storage.get_all_prompts()
    assert len(prompts) == 1


def test_get_prompts_by_collection(storage):
    prompt1 = Prompt(id="1", title="Test1", content="Test content 1", collection_id="col1", created_at=datetime.now(), updated_at=datetime.now())
    prompt2 = Prompt(id="2", title="Test2", content="Test content 2", collection_id="col1", created_at=datetime.now(), updated_at=datetime.now())
    storage.create_prompt(prompt1)
    storage.create_prompt(prompt2)
    prompts = storage.get_prompts_by_collection("col1")
    assert len(prompts) == 2


# ============== Collection Operations Tests ==============

def test_create_collection(storage):
    collection = Collection(id="1", name="Test Collection", created_at=datetime.now())
    result = storage.create_collection(collection)
    assert result.name == "Test Collection"


def test_get_collection(storage):
    collection = Collection(id="1", name="Test Collection", created_at=datetime.now())
    storage.create_collection(collection)
    result = storage.get_collection("1")
    assert result is not None
    assert result.name == "Test Collection"


def test_delete_collection(storage):
    collection = Collection(id="1", name="Test Collection", created_at=datetime.now())
    storage.create_collection(collection)
    result = storage.delete_collection("1")
    assert result is True


def test_get_all_collections(storage):
    collection = Collection(id="1", name="Test Collection", created_at=datetime.now())
    storage.create_collection(collection)
    collections = storage.get_all_collections()
    assert len(collections) == 1


def test_clear_storage(storage):
    collection = Collection(id="1", name="Test Collection", created_at=datetime.now())
    prompt = Prompt(id="1", title="Test Prompt", content="Content", created_at=datetime.now(), updated_at=datetime.now())
    storage.create_collection(collection)
    storage.create_prompt(prompt)
    storage.clear()
    assert len(storage.get_all_prompts()) == 0
    assert len(storage.get_all_collections()) == 0
