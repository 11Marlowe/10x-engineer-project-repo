# Tagging System Feature Specification

## Overview of Tagging Feature
The tagging feature allows users to associate tags with prompts to categorize and filter them based on specific keywords or topics. Tags can enhance the organization and searchability of prompts within the system.

## User Stories with Acceptance Criteria

### User Story 1: Add Tags to Prompts
**As a** user,
**I want** to add tags to my prompts,
**so that** I can categorize them and make them easier to find later.

**Acceptance Criteria:**
- Users can assign multiple tags to a single prompt.
- Tags are unique identifiers and cannot contain special characters.

### User Story 2: Filter Prompts by Tag
**As a** user,
**I want** to filter prompts by tags,
**so that** I can quickly locate relevant prompts based on specific topics.

**Acceptance Criteria:**
- Users can filter the prompt list by selecting one or more tags.
- Only prompts containing all selected tags are displayed.

### User Story 3: Manage Tags
**As a** user,
**I want** to manage the tags I have created,
**so that** I can keep my tagging system organized.

**Acceptance Criteria:**
- Users can view a list of all tags they have created.
- Users can delete tags, which removes the tag from all associated prompts.

## Data Model Changes Needed
- Introduce a new `Tag` model:
  ```python
  class Tag(BaseModel):
      id: str
      name: str
  ```
- Update the `Prompt` model to include a list of tags:
  ```python
  class Prompt(PromptBase):
      # ... existing fields ...
      tags: List[Tag] = []
  ```

## API Endpoint Specifications

### GET /tags
- **Description**: Retrieve a list of all tags.
- **Response**: List of tags.
- **Example Request**:
  ```bash
  curl -X GET "http://localhost:8000/tags"
  ```

### POST /prompts/{prompt_id}/tags
- **Description**: Add tags to a specific prompt.
- **Request Body**: List of tag names to be added.
- **Example Request**:
  ```bash
  curl -X POST "http://localhost:8000/prompts/{id}/tags" -H "Content-Type: application/json" -d '{"tags": ["urgent", "idea"]}'
  ```

### DELETE /prompts/{prompt_id}/tags
- **Description**: Remove tags from a specific prompt.
- **Request Body**: List of tag names to be removed.
- **Example Request**:
  ```bash
  curl -X DELETE "http://localhost:8000/prompts/{id}/tags" -H "Content-Type: application/json" -d '{"tags": ["urgent", "idea"]}'
  ```

## Search/Filter Requirements
- Modify the `GET /prompts` endpoint to accept a `tags` query parameter for filtering based on tags.
- The prompts should support tag filtering where multiple tags can be selected, and prompts must match all specified tags to be included in the results.