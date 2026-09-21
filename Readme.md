# Student Management System API

A RESTful API built with **FastAPI** for managing student records.

The API provides complete CRUD operations, Pydantic validation, custom error handling, filtering, automatic API documentation, and automated testing.

---

## 📌 Project Overview

The **Student Management System API** is a backend application that manages student records through RESTful API endpoints.

The project demonstrates:

* REST API development using FastAPI
* CRUD operations
* Pydantic data validation
* Custom exception handling
* Consistent JSON error responses
* Query parameter filtering
* Clean multi-file project architecture
* Swagger UI and ReDoc documentation
* Automated testing using pytest

The application currently uses an **in-memory data store**, so no external database is required.

---

## 🚀 Features

* Create a student
* Get all students
* Get a student by ID
* Update an entire student
* Partially update a student
* Delete a student
* Filter students by department
* Filter students by minimum age
* Filter students by maximum age
* Pydantic request validation
* Custom 404 error handling
* Custom 422 validation error handling
* Generic 500 error handling
* Swagger UI documentation
* ReDoc documentation
* Automated API testing

---

## 🛠️ Technology Stack

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Programming language |
| FastAPI    | REST API framework   |
| Pydantic   | Data validation      |
| Uvicorn    | ASGI server          |
| Pytest     | Testing framework    |
| HTTPX      | API testing support  |

---

## 📁 Project Structure

```text
student_api/
│
├── main.py
├── exceptions.py
├── requirements.txt
├── README.md
│
├── routers/
│   ├── __init__.py
│   └── students.py
│
├── schemas/
│   ├── __init__.py
│   └── student.py
│
├── services/
│   ├── __init__.py
│   └── student_service.py
│
└── tests/
    ├── __init__.py
    └── test_students.py
```

### File Description

| File                          | Description                                 |
| ----------------------------- | ------------------------------------------- |
| `main.py`                     | FastAPI application and router registration |
| `exceptions.py`               | Custom exceptions and exception handlers    |
| `routers/students.py`         | Student API endpoints                       |
| `schemas/student.py`          | Pydantic request and response models        |
| `services/student_service.py` | CRUD business logic and in-memory storage   |
| `tests/test_students.py`      | Automated API tests                         |
| `requirements.txt`            | Project dependencies                        |
| `README.md`                   | Project documentation                       |

---

# ⚙️ Installation

## 1. Clone or download the project

Open a terminal and navigate to the project directory:

```bash
cd student_api
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

You should see something similar to:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to:

* View all API endpoints
* View request schemas
* View response schemas
* See validation rules
* Execute API requests directly from the browser

## ReDoc

Open:

```text
http://127.0.0.1:8000/redoc
```

## OpenAPI Schema

The generated OpenAPI specification is available at:

```text
http://127.0.0.1:8000/openapi.json
```

---

# 📋 Student Data Model

A student contains the following fields:

| Field        | Type       | Required      | Validation                       |
| ------------ | ---------- | ------------- | -------------------------------- |
| `id`         | `int`      | Response only | Automatically generated          |
| `name`       | `str`      | Yes           | 2–50 characters                  |
| `age`        | `int`      | Yes           | Greater than 0 and less than 100 |
| `email`      | `EmailStr` | Yes           | Valid email format               |
| `department` | `str`      | Yes           | CSE, ECE, MECH, CIVIL            |
| `marks`      | `float`    | No            | 0–100                            |

### Example Student

```json
{
  "id": 1,
  "name": "Rahul Sharma",
  "age": 21,
  "email": "rahul@example.com",
  "department": "CSE",
  "marks": 87.5
}
```

---

# 🔗 API Endpoints

| Method   | Endpoint                 | Description              | Response                           |
| -------- | ------------------------ | ------------------------ | ---------------------------------- |
| `POST`   | `/students`              | Create a student         | `201 Created`                      |
| `GET`    | `/students`              | Get all students         | `200 OK`                           |
| `GET`    | `/students/{student_id}` | Get student by ID        | `200 OK` / `404 Not Found`         |
| `PUT`    | `/students/{student_id}` | Update complete student  | `200 OK` / `404 Not Found`         |
| `PATCH`  | `/students/{student_id}` | Partially update student | `200 OK` / `404 Not Found`         |
| `DELETE` | `/students/{student_id}` | Delete student           | `204 No Content` / `404 Not Found` |

---

# ➕ Create Student

### Endpoint

```http
POST /students
```

### Request Body

```json
{
  "name": "Rahul Sharma",
  "age": 21,
  "email": "rahul@example.com",
  "department": "CSE",
  "marks": 87.5
}
```

### Response

**Status:** `201 Created`

```json
{
  "id": 1,
  "name": "Rahul Sharma",
  "age": 21,
  "email": "rahul@example.com",
  "department": "CSE",
  "marks": 87.5
}
```

---

# 📖 Get All Students

### Endpoint

```http
GET /students
```

### Response

**Status:** `200 OK`

```json
[
  {
    "id": 1,
    "name": "Rahul Sharma",
    "age": 21,
    "email": "rahul@example.com",
    "department": "CSE",
    "marks": 87.5
  },
  {
    "id": 2,
    "name": "Priya Singh",
    "age": 22,
    "email": "priya@example.com",
    "department": "ECE",
    "marks": 91
  }
]
```

---

# 🔍 Get Student by ID

### Endpoint

```http
GET /students/{student_id}
```

### Example

```http
GET /students/1
```

### Response

**Status:** `200 OK`

```json
{
  "id": 1,
  "name": "Rahul Sharma",
  "age": 21,
  "email": "rahul@example.com",
  "department": "CSE",
  "marks": 87.5
}
```

---

# ✏️ Update Student

The `PUT` endpoint replaces all fields of an existing student.

### Endpoint

```http
PUT /students/{student_id}
```

### Example

```http
PUT /students/1
```

### Request Body

```json
{
  "name": "Rahul Kumar",
  "age": 22,
  "email": "rahulkumar@example.com",
  "department": "ECE",
  "marks": 90
}
```

### Response

**Status:** `200 OK`

```json
{
  "id": 1,
  "name": "Rahul Kumar",
  "age": 22,
  "email": "rahulkumar@example.com",
  "department": "ECE",
  "marks": 90
}
```

---

# 🔧 Partially Update Student

The `PATCH` endpoint updates only the fields supplied in the request.

### Endpoint

```http
PATCH /students/{student_id}
```

### Example

```http
PATCH /students/1
```

### Request Body

```json
{
  "department": "CSE"
}
```

### Response

**Status:** `200 OK`

```json
{
  "id": 1,
  "name": "Rahul Kumar",
  "age": 22,
  "email": "rahulkumar@example.com",
  "department": "CSE",
  "marks": 90
}
```

---

# 🗑️ Delete Student

### Endpoint

```http
DELETE /students/{student_id}
```

### Example

```http
DELETE /students/1
```

### Response

**Status:** `204 No Content`

A successful DELETE request does not return a response body.

---

# 🔎 Filtering Students

The `GET /students` endpoint supports optional filters.

## Filter by Department

```http
GET /students?department=CSE
```

Returns students from the CSE department.

## Filter by Minimum Age

```http
GET /students?min_age=20
```

Returns students whose age is greater than or equal to 20.

## Filter by Maximum Age

```http
GET /students?max_age=25
```

Returns students whose age is less than or equal to 25.

## Combine Filters

```http
GET /students?department=CSE&min_age=18&max_age=25
```

This returns students who:

* Belong to CSE
* Are at least 18 years old
* Are at most 25 years old

---

# ✅ Validation Rules

All request bodies are validated using Pydantic.

## Name

* Required
* Minimum length: `2`
* Maximum length: `50`

Example:

```json
{
  "name": "A"
}
```

This request is rejected because the name is shorter than 2 characters.

## Age

* Required
* Must be greater than `0`
* Must be less than `100`

Example:

```json
{
  "age": 150
}
```

This request is rejected.

## Email

* Required
* Must be a valid email address

Example of an invalid email:

```json
{
  "email": "invalid-email"
}
```

## Department

Allowed departments:

```text
CSE
ECE
MECH
CIVIL
```

Example:

```json
{
  "department": "IT"
}
```

This request is rejected.

## Marks

* Optional
* Minimum: `0`
* Maximum: `100`

Example:

```json
{
  "marks": 105
}
```

This request is rejected.

---

# ⚠️ Error Handling

The API uses a consistent JSON format for errors.

## 404 — Student Not Found

Example:

```http
GET /students/999
```

Response:

```json
{
  "error": true,
  "message": "Student with ID 999 not found"
}
```

---

## 422 — Validation Error

When invalid request data is submitted, FastAPI/Pydantic returns HTTP `422`.

Example response:

```json
{
  "error": true,
  "message": "Validation error",
  "details": [
    {
      "type": "string_too_short",
      "loc": [
        "body",
        "name"
      ],
      "msg": "String should have at least 2 characters"
    }
  ]
}
```

---

## 500 — Internal Server Error

Unexpected application errors are handled without exposing the server's internal stack trace.

Example:

```json
{
  "error": true,
  "message": "Internal server error"
}
```

---

# 🧪 Testing

The project uses **pytest** for automated testing.

Run all tests:

```bash
pytest
```

Run tests with detailed output:

```bash
pytest -v
```

The test suite covers:

* Student creation
* Getting all students
* Getting a student by ID
* Updating students
* Partially updating students
* Deleting students
* 404 errors
* Validation errors
* Filtering
* Invalid input

---

# 📡 Example cURL Requests

## Create Student

```bash
curl -X POST "http://127.0.0.1:8000/students" \
-H "Content-Type: application/json" \
-d '{
  "name": "Amit Verma",
  "age": 21,
  "email": "amit@example.com",
  "department": "CSE",
  "marks": 88.5
}'
```

## Get Students

```bash
curl "http://127.0.0.1:8000/students"
```

## Get Student by ID

```bash
curl "http://127.0.0.1:8000/students/1"
```

## Update Student

```bash
curl -X PUT "http://127.0.0.1:8000/students/1" \
-H "Content-Type: application/json" \
-d '{
  "name": "Amit Kumar",
  "age": 22,
  "email": "amitkumar@example.com",
  "department": "ECE",
  "marks": 92
}'
```

## Partially Update Student

```bash
curl -X PATCH "http://127.0.0.1:8000/students/1" \
-H "Content-Type: application/json" \
-d '{
  "department": "MECH"
}'
```

## Delete Student

```bash
curl -X DELETE "http://127.0.0.1:8000/students/1"
```

---

# 🏗️ Architecture

The project follows a layered architecture.

```text
                Client
                  │
                  ▼
          ┌───────────────┐
          │    FastAPI    │
          │    main.py    │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │    Router     │
          │ students.py   │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │    Service    │
          │ student_      │
          │ service.py    │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │ In-Memory     │
          │ Data Store    │
          └───────────────┘
```

### Schema Layer

Pydantic schemas validate incoming data before it reaches the service layer.

```text
Client Request
      │
      ▼
Pydantic Validation
      │
      ├── Invalid ──► 422 Response
      │
      ▼
    Router
      │
      ▼
   Service
```

### Exception Layer

Errors are handled centrally by custom exception handlers.

```text
Application Error
       │
       ▼
Exception Handler
       │
       ▼
Consistent JSON Response
```

---

# 💾 Data Storage

The application currently uses an in-memory Python dictionary.

Example:

```python
students = {
    1: {
        "id": 1,
        "name": "Rahul Sharma",
        "age": 21,
        "email": "rahul@example.com",
        "department": "CSE",
        "marks": 87.5
    }
}
```

Because the data is stored in memory, all student records are lost when the application restarts.

No external database is required for this version of the project.

---

# 📊 HTTP Status Codes

| Status Code                 | Meaning                        |
| --------------------------- | ------------------------------ |
| `200 OK`                    | Request completed successfully |
| `201 Created`               | Student successfully created   |
| `204 No Content`            | Student successfully deleted   |
| `404 Not Found`             | Student does not exist         |
| `422 Unprocessable Entity`  | Request validation failed      |
| `500 Internal Server Error` | Unexpected server error        |

---

# 🔮 Future Improvements

Possible improvements for future versions include:

* PostgreSQL/MySQL database integration
* SQLAlchemy or SQLModel
* Database migrations
* JWT authentication
* Role-based authorization
* Pagination
* Sorting
* Advanced search
* Student attendance management
* Course management
* Docker support
* CI/CD pipeline
* Cloud deployment
* Production logging

---

# 📝 Capstone Evaluation Checklist

## CRUD Completeness — 20 Points

* [x] `POST /students`
* [x] `GET /students`
* [x] `GET /students/{student_id}`
* [x] `PUT /students/{student_id}`
* [x] `PATCH /students/{student_id}`
* [x] `DELETE /students/{student_id}`

## Validation — 20 Points

* [x] Name validation
* [x] Age validation
* [x] Email validation
* [x] Department validation
* [x] Marks validation
* [x] Pydantic models

## Error Handling — 20 Points

* [x] 404 handling
* [x] 422 validation handling
* [x] Consistent JSON errors
* [x] 500 error handling
* [x] No raw stack traces

## Code Structure — 20 Points

* [x] Router layer
* [x] Schema layer
* [x] Service layer
* [x] Exception layer
* [x] Clean `main.py`

## Documentation & Testing — 20 Points

* [x] Swagger UI
* [x] ReDoc
* [x] OpenAPI documentation
* [x] README
* [x] pytest test suite

---

# 👨‍💻 Project

**Student Management System API**

Built with **Python + FastAPI + Pydantic + Pytest**.

This project demonstrates the development of a structured, validated, documented, and tested REST API.
