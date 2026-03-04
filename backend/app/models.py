"""Pydantic models for PromptLab"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from uuid import uuid4


def generate_id() -> str:
    """Generate a unique identifier for models.

    Returns:
        str: A unique identifier as a string.
    """
    return str(uuid4())


def get_current_time() -> datetime:
    """Get the current UTC time.

    Returns:
        datetime: The current UTC time.
    """
    return datetime.utcnow()


# ============== Prompt Models ==============

class PromptBase(BaseModel):
    """Base model for a Prompt.

    Attributes:
        title (str): The title of the prompt.
        content (str): The content of the prompt.
        description (Optional[str]): An optional description of the prompt.
        collection_id (Optional[str]): The associated collection ID, if any.
    """
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    description: Optional[str] = Field(None, max_length=500)
    collection_id: Optional[str] = None


class PromptCreate(PromptBase):
    """Model for creating a new Prompt. Inherits from PromptBase."""
    pass


class PromptUpdate(PromptBase):
    """Model for updating an existing Prompt. Inherits from PromptBase.

    Attributes are optional to allow for partial updates.
    """
    title: Optional[str] = None
    content: Optional[str] = None
    description: Optional[str] = None
    collection_id: Optional[str] = None


class Prompt(PromptBase):
    """Model representing a complete Prompt, including metadata.

    Attributes:
        id (str): Unique identifier for the prompt.
        created_at (datetime): Timestamp of creation.
        updated_at (datetime): Timestamp of last update.
    """
    id: str = Field(default_factory=generate_id)
    created_at: datetime = Field(default_factory=get_current_time)
    updated_at: datetime = Field(default_factory=get_current_time)
    tags: List[str] = []  # Add a list of tag names

    class Config:
        from_attributes = True



# ============== Collection Models ==============

class CollectionBase(BaseModel):
    """Base model for a Collection.

    Attributes:
        name (str): The name of the collection.
        description (Optional[str]): An optional description of the collection.
    """
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)


class CollectionCreate(CollectionBase):
    """Model for creating a new Collection. Inherits from CollectionBase."""
    pass


class Collection(CollectionBase):
    """Model representing a complete Collection, including metadata.

    Attributes:
        id (str): Unique identifier for the collection.
        created_at (datetime): Timestamp of creation.
    """
    id: str = Field(default_factory=generate_id)
    created_at: datetime = Field(default_factory=get_current_time)

    class Config:
        from_attributes = True


# ============== Response Models ==============

class PromptList(BaseModel):
    """Model for a list of Prompts, including the total count.

    Attributes:
        prompts (List[Prompt]): A list of prompt objects.
        total (int): Total number of prompts available.
    """
    prompts: List[Prompt]
    total: int


class CollectionList(BaseModel):
    """Model for a list of Collections, including the total count.

    Attributes:
        collections (List[Collection]): A list of collection objects.
        total (int): Total number of collections available.
    """
    collections: List[Collection]
    total: int


class HealthResponse(BaseModel):
    """Model representing the health status and version of the application.

    Attributes:
        status (str): Health status of the application (e.g., 'healthy').
        version (str): Application version number.
    """
    status: str
    version: str

class Tag(BaseModel):
    """Model for a Tag."""
    id: str = Field(default_factory=generate_id)
    name: str = Field(..., min_length=1, max_length=50)

class TagsData(BaseModel):
    tags: List[str]



