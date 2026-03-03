"""FastAPI routes for PromptLab"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from app.models import (
    Prompt, PromptCreate, PromptUpdate,
    Collection, CollectionCreate,
    PromptList, CollectionList, HealthResponse,
    get_current_time
)
from app.storage import storage
from app.utils import sort_prompts_by_date, filter_prompts_by_collection, search_prompts
from app import __version__


app = FastAPI(
    title="PromptLab API",
    description="AI Prompt Engineering Platform",
    version=__version__
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============== Health Check ==============

@app.get("/health", response_model=HealthResponse)
def health_check():
    """Check the health status of the API service.

    Returns:
        HealthResponse: JSON response with the status and version of the API.

    Example:
        >>> curl -X GET "http://localhost:8000/health"
    """
    return HealthResponse(status="healthy", version=__version__)


# ============== Prompt Endpoints ==============

@app.get("/prompts", response_model=PromptList)
def list_prompts(
    collection_id: Optional[str] = None,
    search: Optional[str] = None
):
    """List all prompts, with optional filtering and searching.

    Args:
        collection_id (Optional[str]): ID of the collection to filter prompts.
        search (Optional[str]): Query string to search for in prompt titles and descriptions.

    Returns:
        PromptList: A list of prompts and the total count.

    Example:
        >>> curl -X GET "http://localhost:8000/prompts?collection_id=123&search=example"
    """
    prompts = storage.get_all_prompts()
    
    # Filter by collection if specified
    if collection_id:
        prompts = filter_prompts_by_collection(prompts, collection_id)
    
    # Search if query provided
    if search:
        prompts = search_prompts(prompts, search)
    
    # Sort by date (newest first)
    # Note: There might be an issue with the sorting...
    prompts = sort_prompts_by_date(prompts, descending=True)
    
    return PromptList(prompts=prompts, total=len(prompts))


@app.get("/prompts/{prompt_id}", response_model=Prompt)
def get_prompt(prompt_id: str):
    """Retrieve a specific prompt by its ID.

    Args:
        prompt_id (str): The ID of the prompt to retrieve.

    Returns:
        Prompt: The prompt object if found.

    Raises:
        HTTPException: If the prompt does not exist (404 error).

    Example:
        >>> curl -X GET "http://localhost:8000/prompts/123"
    """
    prompt = storage.get_prompt(prompt_id)

    if prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found")
    
    # This line causes the bug - accessing attribute on None
    if prompt.id:
        return prompt


@app.post("/prompts", response_model=Prompt, status_code=201)
def create_prompt(prompt_data: PromptCreate):
    """Create a new prompt.

    Args:
        prompt_data (PromptCreate): Data for the new prompt.

    Returns:
        Prompt: The created prompt object.

    Raises:
        HTTPException: If the specified collection does not exist (400 error).

    Example:
        >>> curl -X POST "http://localhost:8000/prompts" -H "Content-Type: application/json" -d '{"title": "New Prompt", "content": "..."}'
    """
    # Validate collection exists if provided
    if prompt_data.collection_id:
        collection = storage.get_collection(prompt_data.collection_id)
        if not collection:
            raise HTTPException(status_code=400, detail="Collection not found")
    
    prompt = Prompt(**prompt_data.model_dump())
    return storage.create_prompt(prompt)


@app.put("/prompts/{prompt_id}", response_model=Prompt)
def update_prompt(prompt_id: str, prompt_data: PromptUpdate):
    """Update an existing prompt completely.

    Args:
        prompt_id (str): The ID of the prompt to update.
        prompt_data (PromptUpdate): Updated prompt data.

    Returns:
        Prompt: The updated prompt object.

    Raises:
        HTTPException: If the prompt or collection does not exist (404 or 400 error).

    Example:
        >>> curl -X PUT "http://localhost:8000/prompts/123" -H "Content-Type: application/json" -d '{"title": "Updated Prompt"}'
    """
    existing = storage.get_prompt(prompt_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Prompt not found")
    
    # Validate collection if provided
    if prompt_data.collection_id:
        collection = storage.get_collection(prompt_data.collection_id)
        if not collection:
            raise HTTPException(status_code=400, detail="Collection not found")
    
    # BUG #2: We're not updating the updated_at timestamp!
    # The updated prompt keeps the old timestamp
    updated_prompt = Prompt(
        id=existing.id,
        title=prompt_data.title,
        content=prompt_data.content,
        description=prompt_data.description,
        collection_id=prompt_data.collection_id,
        created_at=existing.created_at,
        updated_at=get_current_time()  # BUG: Should be get_current_time()
    )
    
    return storage.update_prompt(prompt_id, updated_prompt)


# NOTE: PATCH endpoint is missing! Students need to implement this.
# It should allow partial updates (only update provided fields)


@app.delete("/prompts/{prompt_id}", status_code=204)
def delete_prompt(prompt_id: str):
    """Delete a prompt by its ID.

    Args:
        prompt_id (str): The ID of the prompt to delete.

    Returns:
        None

    Raises:
        HTTPException: If the prompt does not exist (404 error).

    Example:
        >>> curl -X DELETE "http://localhost:8000/prompts/123"
    """
    if not storage.delete_prompt(prompt_id):
        raise HTTPException(status_code=404, detail="Prompt not found")
    return None


# ============== Collection Endpoints ==============

@app.get("/collections", response_model=CollectionList)
def list_collections():
    """List all collections.

    Returns:
        CollectionList: A list of collections and the total count.

    Example:
        >>> curl -X GET "http://localhost:8000/collections"
    """
    collections = storage.get_all_collections()
    return CollectionList(collections=collections, total=len(collections))


@app.get("/collections/{collection_id}", response_model=Collection)
def get_collection(collection_id: str):
    """Retrieve a specific collection by its ID.

    Args:
        collection_id (str): The ID of the collection to retrieve.

    Returns:
        Collection: The collection object if found.

    Raises:
        HTTPException: If the collection does not exist (404 error).

    Example:
        >>> curl -X GET "http://localhost:8000/collections/123"
    """
    collection = storage.get_collection(collection_id)
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")
    return collection


@app.post("/collections", response_model=Collection, status_code=201)
def create_collection(collection_data: CollectionCreate):
    """Create a new collection.

    Args:
        collection_data (CollectionCreate): Data for the new collection.

    Returns:
        Collection: The created collection object.

    Example:
        >>> curl -X POST "http://localhost:8000/collections" -H "Content-Type: application/json" -d '{"name": "New Collection"}'
    """
    collection = Collection(**collection_data.model_dump())
    return storage.create_collection(collection)


@app.delete("/collections/{collection_id}", status_code=204)
def delete_collection(collection_id: str):
    """Delete a collection by its ID.

    Args:
        collection_id (str): The ID of the collection to delete.

    Returns:
        None

    Raises:
        HTTPException: If the collection does not exist (404 error).

    Example:
        >>> curl -X DELETE "http://localhost:8000/collections/123"
    """
    
    prompts = storage.get_prompts_by_collection(collection_id)
    
    if not storage.delete_collection(collection_id):
        raise HTTPException(status_code=404, detail="Collection not found")
    
    for prompt in prompts:
        prompt.collection_id = None
        # Save the updated prompt back to the storage
        storage.update_prompt(prompt.id, prompt)
    
    return None

@app.patch("/prompts/{prompt_id}", response_model=Prompt)
def patch_prompt(prompt_id: str, prompt_data: PromptUpdate):
    """Partially update an existing prompt.

    Args:
        prompt_id (str): The ID of the prompt to update.
        prompt_data (PromptUpdate): Partial prompt data.

    Returns:
        Prompt: The updated prompt object.

    Raises:
        HTTPException: If the prompt does not exist (404 error).

    Example:
        >>> curl -X PATCH "http://localhost:8000/prompts/123" -H "Content-Type: application/json" -d '{"title": "Partially Updated Prompt"}'
    """
    existing_prompt = storage.get_prompt(prompt_id)
    if not existing_prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")

    # Update fields only if they are provided in the request
    update_data = prompt_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(existing_prompt, key, value)

    # Optionally, update the updated_at timestamp
    existing_prompt.updated_at = get_current_time()

    # Save the updated prompt
    return storage.update_prompt(prompt_id, existing_prompt)

@app.post("/prompts/{prompt_id}/tags")
def add_tags_to_prompt(prompt_id: str, tags: List[str]):
    prompt = storage.add_tags_to_prompt(prompt_id, tags)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return prompt

@app.delete("/prompts/{prompt_id}/tags")
def remove_tags_from_prompt(prompt_id: str, tags: List[str]):
    prompt = storage.remove_tags_from_prompt(prompt_id, tags)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return prompt

@app.get("/tags")
def get_all_tags() -> List[str]:
    prompts = storage.get_all_prompts()
    tags = {tag for prompt in prompts for tag in prompt.tags}
    return list(tags)