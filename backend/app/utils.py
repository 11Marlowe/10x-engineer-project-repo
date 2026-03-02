"""Utility functions for PromptLab"""

from typing import List
from app.models import Prompt


def sort_prompts_by_date(prompts: List[Prompt], descending: bool = True) -> List[Prompt]:
    """Sort prompts by creation date.

    Args:
        prompts (List[Prompt]): A list of prompts to sort.
        descending (bool): Whether to sort in descending order. Defaults to True.

    Returns:
        List[Prompt]: List of prompts sorted by creation date.

    Example:
        >>> sorted_prompts = sort_prompts_by_date(prompts)
        >>> print([p.created_at for p in sorted_prompts])
        [datetime(2023, 10, 1), datetime(2023, 9, 28)]
    """
    # BUG #3: This sorts ascending (oldest first) when it should sort descending (newest first)
    # The 'descending' parameter is ignored!
    return sorted(prompts, key=lambda p: p.created_at, reverse=descending)


def filter_prompts_by_collection(prompts: List[Prompt], collection_id: str) -> List[Prompt]:
    """Filter prompts by collection ID.

    Args:
        prompts (List[Prompt]): A list of prompts to filter.
        collection_id (str): The collection ID to filter prompts by.

    Returns:
        List[Prompt]: List of prompts belonging to the specified collection.

    Example:
        >>> filtered_prompts = filter_prompts_by_collection(prompts, "collection123")
        >>> print(len(filtered_prompts))
        5
    """
    return [p for p in prompts if p.collection_id == collection_id]


def search_prompts(prompts: List[Prompt], query: str) -> List[Prompt]:
    """Search for prompts that contain a query in the title or description.

    Args:
        prompts (List[Prompt]): A list of prompts to search.
        query (str): The query string to search for.

    Returns:
        List[Prompt]: List of prompts matching the search query.

    Example:
        >>> results = search_prompts(prompts, "example query")
        >>> print([p.title for p in results])
        ["Example Prompt 1"]
    """
    query_lower = query.lower()
    return [
        p for p in prompts 
        if query_lower in p.title.lower() or 
           (p.description and query_lower in p.description.lower())
    ]


def validate_prompt_content(content: str) -> bool:
    """Check if prompt content is valid.
    
    Args:
        content (str): The content string to validate.

    Returns:
        bool: True if content is valid, False otherwise.

    A valid prompt should:
    - Not be empty
    - Not be just whitespace
    - Be at least 10 characters

    Example:
        >>> is_valid = validate_prompt_content("   ")
        >>> print(is_valid)
        False
    """
    if not content or not content.strip():
        return False
    return len(content.strip()) >= 10


def extract_variables(content: str) -> List[str]:
    """Extract template variables from prompt content.

    Args:
        content (str): The prompt content containing variables.

    Returns:
        List[str]: List of variable names found in the content.

    Variables are in the format {{variable_name}}.

    Example:
        >>> variables = extract_variables("{{user}} will do something with {{tool}}.")
        >>> print(variables)
        ['user', 'tool']
    """
    import re
    pattern = r'\{\{(\w+)\}\}'
    return re.findall(pattern, content)
