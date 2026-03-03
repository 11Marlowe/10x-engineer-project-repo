# PromptLab

## Project Overview and Purpose
PromptLab is an application designed to facilitate the management and execution of creative prompts. Developed over a 4-week cycle, the project evolves into a production-ready, full-stack application.

## Features List
- API for prompt management
- Collection handling
- Persistent storage
- Full CRUD operations for prompts and collections
- Advanced sorting and filtering capabilities

## Prerequisites and Installation
- Python 3.10 or later
- Node.js and npm
- Docker (optional, for containerization)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Set up the backend:
   ```bash
   cd backend
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```
3. Set up the frontend:
   ```bash
   cd frontend
   npm install
   ```
4. (Optional) To use Docker:
   ```bash
   docker-compose up --build
   ```

## Quick Start Guide
1. **Run the backend:**
   ```bash
   cd backend
   python main.py
   ```
2. **Run the frontend:**
   ```bash
   cd frontend
   npm start
   ```
3. Open your browser and navigate to `http://localhost:3000` to interact with the application.

## API Endpoint Summary with Examples
- **GET /prompts** - List all prompts
- **POST /prompts** - Create a new prompt
- **GET /prompts/{id}** - Retrieve a specific prompt
- **PUT /prompts/{id}** - Update an entire prompt
- **PATCH /prompts/{id}** - Partially update a prompt
- **DELETE /prompts/{id}** - Delete a prompt

**Example:**
```bash
GET /prompts
Response:
{
  "data": [...],
  "total": 100
}
```

## Development Setup
1. Ensure all prerequisites are installed.
2. Follow the installation steps for both backend and frontend.
3. Use `pytest` to run backend tests:
   ```bash
   pytest tests/ -v
   ```
4. For frontend development, ensure Vite is set up.
5. Utilize Docker setup for consistent environments.

## Contributing Guidelines
- Fork the repository.
- Create a branch for your feature or bugfix.
- Commit your changes with clear messages.
- Submit a pull request for review.
- Follow coding standards as outlined in `.github/copilot-instructions.md`.

For more detailed development guidelines, please refer to the `PROJECT_BRIEF.md` and specific spec files in the `specs/` directory.
