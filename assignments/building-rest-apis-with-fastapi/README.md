# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice defining endpoints, validating request data, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create the FastAPI application

#### Description
Set up a new FastAPI application with a root endpoint and a running app instance.

#### Requirements
Completed program should:

- Create a `FastAPI()` app instance.
- Define a root endpoint at `/` that returns a welcome message.
- Include a sample `/items` endpoint that returns a list of items.

### 🛠️ Define API models and routes

#### Description
Use Pydantic models to validate input and build endpoints for reading and creating items.

#### Requirements
Completed program should:

- Define an `Item` model with fields such as `id`, `name`, `description`, and `price`.
- Add a `GET /items/{item_id}` endpoint to retrieve a specific item.
- Add a `POST /items` endpoint that accepts JSON data and returns the created item.
- Return an error response if a requested item is not found.

### 🛠️ Handle request data and responses

#### Description
Implement JSON request handling and clear API responses for success and failure cases.

#### Requirements
Completed program should:

- Validate incoming POST request data against the `Item` model.
- Return JSON responses with appropriate status and data.
- Use `HTTPException` or similar error handling for invalid item lookups.
- Keep all API data in memory for this assignment (no database required).
