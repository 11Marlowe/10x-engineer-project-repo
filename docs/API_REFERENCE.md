# API Reference Documentation

## Authentication
Currently, there is no authentication required for accessing the API endpoints.

## Endpoints

### Health Check

#### GET /health
- **Description**: Check the health status of the API service.
- **Response**: JSON object with the status and version of the API.
- **Example Request**:
  ```bash
  curl -X GET "http://localhost:8000/health"
  ```
- **Example Response**:
  ```json
  {
    "status": "healthy",
    "version": "1.0"
  }
  ```

---

### Prompt Endpoints

#### GET /prompts
- **Description**: List all prompts, with optional filtering by collection ID and search query.
- **Query Parameters**:
  - `collection_id` (optional): Filter prompts by collection.
  - `search` (optional): Search prompts by title or description.
- **Response**: List of prompt objects and total count.
- **Example Request**:
  ```bash
  curl -X GET "http://localhost:8000/prompts?collection_id=123&search=example"
  ```
- **Example Response**:
  ```json
  {
    "prompts": [...],
    "total": 10
  }
  ```

#### GET /prompts/{prompt_id}
- **Description**: Retrieve a specific prompt by its ID.
- **Path Parameters**:
  - `prompt_id`: ID of the prompt to retrieve.
- **Response**: Prompt object if found.
- **Error Responses**:
  - 404: Prompt not found.
- **Example Request**:
  ```bash
  curl -X GET "http://localhost:8000/prompts/1"
  ```
- **Example Error Response**:
  ```json
  {
    "detail": "Prompt not found"
  }
  ```

#### POST /prompts
- **Description**: Create a new prompt.
- **Request Body**: PromptCreate object with title, content, description, and collection_id (if any).
- **Response**: Created prompt object.
- **Error Responses**:
  - 400: Collection not found if invalid collection_id is provided.
- **Example Request**:
  ```bash
  curl -X POST "http://localhost:8000/prompts" -H "Content-Type: application/json" -d '{"title": "New Prompt", "content": "..."}'
  ```
- **Example Error Response**:
  ```json
  {
    "detail": "Collection not found"
  }
  ```

#### PUT /prompts/{prompt_id}
- **Description**: Update an existing prompt completely.
- **Request Body**: PromptUpdate object with updated fields.
- **Error Responses**:
  - 404: Prompt not found.
  - 400: Collection not found if invalid collection_id is provided.
- **Example Request**:
  ```bash
  curl -X PUT "http://localhost:8000/prompts/1" -H "Content-Type: application/json" -d '{"title": "Updated Title"}'
  ```

#### PATCH /prompts/{prompt_id}
- **Description**: Partially update an existing prompt.
- **Request Body**: Partial data for the prompt.
- **Error Responses**:
  - 404: Prompt not found.
- **Example Request**:
  ```bash
  curl -X PATCH "http://localhost:8000/prompts/1" -H "Content-Type: application/json" -d '{"title": "Partially Updated Title"}'
  ```

#### DELETE /prompts/{prompt_id}
- **Description**: Delete a prompt by its ID.
- **Error Responses**:
  - 404: Prompt not found.
- **Example Request**:
  ```bash
  curl -X DELETE "http://localhost:8000/prompts/1"
  ```

---

### Collection Endpoints

#### GET /collections
- **Description**: List all collections.
- **Response**: List of collection objects and total count.
- **Example Request**:
  ```bash
  curl -X GET "http://localhost:8000/collections"
  ```

#### GET /collections/{collection_id}
- **Description**: Retrieve a specific collection by its ID.
- **Path Parameters**:
  - `collection_id`: ID of the collection to retrieve.
- **Response**: Collection object if found.
- **Example Request**:
  ```bash
  curl -X GET "http://localhost:8000/collections/1"
  ```

#### POST /collections
- **Description**: Create a new collection.
- **Request Body**: CollectionCreate object with name and description.
- **Response**: Created collection object.
- **Example Request**:
  ```bash
  curl -X POST "http://localhost:8000/collections" -H "Content-Type: application/json" -d '{"name": "New Collection", "description": "..."}'
  ```

#### DELETE /collections/{collection_id}
- **Description**: Delete a collection by its ID.
- **Path Parameters**:
  - `collection_id`: ID of the collection to delete.
- **Error Responses**:
  - 404: Collection not found.
- **Example Request**:
  ```bash
  curl -X DELETE "http://localhost:8000/collections/1"
  ```
- **Example Error Response**:
  ```json
  {
    "detail": "Collection not found"
  }
  ```