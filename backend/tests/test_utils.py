import pytest
from datetime import datetime
from app.models import Prompt
from app.utils import (
    sort_prompts_by_date,
    filter_prompts_by_collection,
    search_prompts,
    validate_prompt_content,
    extract_variables
)


# ============== Tests for sort_prompts_by_date ==============

def test_sort_prompts_by_date():
    prompt1 = Prompt(id="1", title="First", content="Content 1", created_at=datetime(2023, 1, 1), updated_at=datetime(2023, 1, 1))
    prompt2 = Prompt(id="2", title="Second", content="Content 2", created_at=datetime(2023, 2, 1), updated_at=datetime(2023, 2, 1))
    prompts = [prompt1, prompt2]
    sorted_prompts = sort_prompts_by_date(prompts)
    assert sorted_prompts[0].title == "Second"


# ============== Tests for filter_prompts_by_collection ==============

def test_filter_prompts_by_collection():
    prompt1 = Prompt(id="1", title="First", content="Content 1", collection_id="col1", created_at=datetime.now(), updated_at=datetime.now())
    prompt2 = Prompt(id="2", title="Second", content="Content 2", collection_id="col2", created_at=datetime.now(), updated_at=datetime.now())
    prompts = [prompt1, prompt2]
    filtered_prompts = filter_prompts_by_collection(prompts, "col1")
    assert len(filtered_prompts) == 1
    assert filtered_prompts[0].collection_id == "col1"


# ============== Tests for search_prompts ==============

def test_search_prompts():
    prompt1 = Prompt(id="1", title="First", description="Desc 1", content="Content 1", created_at=datetime.now(), updated_at=datetime.now())
    prompt2 = Prompt(id="2", title="Second", description="Desc 2", content="Content 2", created_at=datetime.now(), updated_at=datetime.now())
    prompts = [prompt1, prompt2]
    search_results = search_prompts(prompts, "first")
    assert len(search_results) == 1
    assert search_results[0].title == "First"


# ============== Tests for validate_prompt_content ==============

def test_validate_prompt_content():
    valid_content = "This is valid content."
    invalid_content = "   "
    assert validate_prompt_content(valid_content) is True
    assert validate_prompt_content(invalid_content) is False


# ============== Tests for extract_variables ==============

def test_extract_variables():
    content = "Use variables like {{variable1}} and {{variable2}}."
    variables = extract_variables(content)
    assert variables == ["variable1", "variable2"]
