# Prompt Versions Feature Specification

## Overview of Version Tracking Feature
The version tracking feature allows users to maintain a history of changes for each prompt. Every time a prompt is modified, a new version is created and stored, enabling users to view previous versions and revert if necessary.

## User Stories with Acceptance Criteria

### User Story 1: View Prompt Versions
**As a** user,
**I want** to view the history of changes made to a prompt,
**so that** I can track the changes over time.

**Acceptance Criteria:**
- When viewing a prompt, users can see a list of all previous versions with timestamps and changes made.
- Each version entry shows a summary of changes, including content and title updates.

### User Story 2: Revert to Previous Version
**As a** user,
**I want** to revert a prompt to a previous version,
**so that** I can restore it to a known good state if a mistake is made.

**Acceptance Criteria:**
- Users can select a version from the history and revert the prompt to that version.
- Reverting creates a new version with the restored content.
- Confirmation is required before reverting changes.

## Data Model Changes Needed
- Introduce a new `PromptVersion` model:
  ```python
  class PromptVersion(BaseModel):
      prompt_id: str
      version_number: int
      title: str
      content: str
      description: Optional[str]
      created_at: datetime
  ```
- Update the `Prompt` model to include the current `version_number`.

## API Endpoint Specifications

### GET /prompts/{prompt_id}/versions
- **Description**: Retrieve all versions for a specific prompt.
- **Response**: List of prompt versions.
- **Example Request**:
  ```bash
  curl -X GET "http://localhost:8000/prompts/{id}/versions"
  ```
- **Example Response**:
  ```json
  [
    {
      "version_number": 1,
      "title": "Initial Version",
      "content": "...
  }
  ```

### POST /prompts/{prompt_id}/revert
- **Description**: Revert a prompt to a previous version.
- **Request Body**: The `version_number` to revert to.
- **Example Request**:
  ```bash
  curl -X POST "http://localhost:8000/prompts/{id}/revert" -H "Content-Type: application/json" -d '{"version_number": 2}'
  ```

## Edge Cases to Handle
- Changes made without any modification (e.g., same title/content) should not create a new version.
- Reverting to the current version should not duplicate the version.
- Ensure that reverting does not break the referential integrity of collections or other dependencies associated with the prompt.
- Handle concurrent modifications to avoid race conditions when multiple users are updating the same prompt.