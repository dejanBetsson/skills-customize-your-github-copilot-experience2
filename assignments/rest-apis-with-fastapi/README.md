# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using Python and the FastAPI framework, practicing route creation, request handling, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application

#### Description
Install FastAPI and create a basic application with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install `fastapi` and `uvicorn` using pip
- Create a FastAPI app instance in `main.py`
- Define a `GET /` route that returns a JSON welcome message
- Run the app with `uvicorn` and verify it works in the browser or with curl

Example output:
```json
{"message": "Welcome to the Student API!"}
```


### 🛠️ Build a Students CRUD API

#### Description
Extend the application by adding endpoints to create, read, update, and delete student records stored in an in-memory list.

#### Requirements
Completed program should:

- Define a `Student` model using Pydantic with fields: `id` (int), `name` (str), and `grade` (str)
- Implement `GET /students` to return all students
- Implement `POST /students` to add a new student
- Implement `GET /students/{id}` to retrieve a single student by ID
- Implement `DELETE /students/{id}` to remove a student by ID
- Return a `404` HTTP error when a student ID is not found

Example input for `POST /students`:
```json
{"id": 1, "name": "Alice", "grade": "A"}
```
