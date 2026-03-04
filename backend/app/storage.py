"""In-memory storage for PromptLab

This module provides simple in-memory storage for prompts and collections.
In a production environment, this would be replaced with a database.
"""

from typing import Dict, List, Optional
from app.models import Prompt, Collection


class Storage:
    """In-memory storage class for managing Prompts and Collections.

    This class simulates a database by using Python dictionaries to store prompts and collections.
    It's used for development and testing purposes.
    """
    def __init__(self):
        """Initialize the Storage with empty dictionaries for prompts and collections."""
        self._prompts: Dict[str, Prompt] = {}
        self._collections: Dict[str, Collection] = {}
    
    # ============== Prompt Operations ==============
    
    def create_prompt(self, prompt: Prompt) -> Prompt:
        """Create a new prompt and add it to storage.
        
        Args:
            prompt (Prompt): The prompt to be added.

        Returns:
            Prompt: The created prompt object.
        """
        self._prompts[prompt.id] = prompt
        return prompt
    
    def get_prompt(self, prompt_id: str) -> Optional[Prompt]:
        """Retrieve a prompt by its ID.

        Args:
            prompt_id (str): The ID of the prompt to retrieve.

        Returns:
            Optional[Prompt]: The prompt object if found, else None.
        """
        return self._prompts.get(prompt_id)
    
    def get_all_prompts(self) -> List[Prompt]:
        """Retrieve all prompts from storage.

        Returns:
            List[Prompt]: A list containing all stored prompts.
        """
        return list(self._prompts.values())
    
    def update_prompt(self, prompt_id: str, prompt: Prompt) -> Optional[Prompt]:
        """Update an existing prompt.

        Args:
            prompt_id (str): The ID of the prompt to update.
            prompt (Prompt): The new prompt data.

        Returns:
            Optional[Prompt]: The updated prompt object if successful, else None.
        """
        if prompt_id not in self._prompts:
            return None
        self._prompts[prompt_id] = prompt
        return prompt
    
    def delete_prompt(self, prompt_id: str) -> bool:
        """Delete a prompt by its ID.

        Args:
            prompt_id (str): The ID of the prompt to delete.

        Returns:
            bool: True if deletion was successful, False if prompt was not found.
        """
        if prompt_id in self._prompts:
            del self._prompts[prompt_id]
            return True
        return False
    
    # ============== Collection Operations ==============
    
    def create_collection(self, collection: Collection) -> Collection:
        """Create a new collection and add it to storage.

        Args:
            collection (Collection): The collection to be added.

        Returns:
            Collection: The created collection object.
        """
        self._collections[collection.id] = collection
        return collection
    
    def get_collection(self, collection_id: str) -> Optional[Collection]:
        """Retrieve a collection by its ID.

        Args:
            collection_id (str): The ID of the collection to retrieve.

        Returns:
            Optional[Collection]: The collection object if found, else None.
        """
        return self._collections.get(collection_id)
    
    def get_all_collections(self) -> List[Collection]:
        """Retrieve all collections from storage.

        Returns:
            List[Collection]: A list containing all stored collections.
        """
        return list(self._collections.values())
    
    def delete_collection(self, collection_id: str) -> bool:
        """Delete a collection by its ID.

        Args:
            collection_id (str): The ID of the collection to delete.

        Returns:
            bool: True if deletion was successful, False if collection was not found.
        """
        if collection_id in self._collections:
            del self._collections[collection_id]
            return True
        return False
    
    def get_prompts_by_collection(self, collection_id: str) -> List[Prompt]:
        """Retrieve all prompts belonging to a specific collection.

        Args:
            collection_id (str): The ID of the collection.

        Returns:
            List[Prompt]: A list of prompts belonging to the specified collection.
        """
        return [p for p in self._prompts.values() if p.collection_id == collection_id]
    
    # ============== Utility ==============
    
    def clear(self):
        """Clear all prompts and collections from storage."""
        self._prompts.clear()
        self._collections.clear()

    def add_tags_to_prompt(self, prompt_id: str, tags: List[str]) -> Optional[Prompt]:
        """Add tags to a prompt.

        Args:
            prompt_id (str): The ID of the prompt to add tags to.
            tags (List[str]): A list of tags to be added to the prompt.

        Returns:
            Optional[Prompt]: The updated prompt object if successful, else None.
        """
        prompt = self.get_prompt(prompt_id)
        if not prompt:
            return None
        # Add tags only if they are not already present
        prompt.tags.extend(tag for tag in tags if tag not in prompt.tags)
        return self.update_prompt(prompt_id, prompt)

    def remove_tags_from_prompt(self, prompt_id: str, tags: List[str]) -> Optional[Prompt]:
        """Remove tags from a prompt.

        Args:
            prompt_id (str): The ID of the prompt to remove tags from.
            tags (List[str]): A list of tags to be removed from the prompt.

        Returns:
            Optional[Prompt]: The updated prompt object if successful, else None.
        """
        prompt = self.get_prompt(prompt_id)
        if not prompt:
            return None
        # Remove specified tags
        prompt.tags = [tag for tag in prompt.tags if tag not in tags]
        return self.update_prompt(prompt_id, prompt)

# Global storage instance
storage = Storage()


