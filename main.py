from fastapi import FastAPI

from routers.students import router as students_router
from exceptions import (
    StudentNotFoundException,
    student_not_found_handler,
    validation_exception_handler,
    http_exception_handler,
    general_exception_handler,
)

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException


app = FastAPI(
    title="Student Management System API",
    description="REST API for managing student records",
    version="1.0.0",
)



app.add_exception_handler(
    StudentNotFoundException,
    student_not_found_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.add_exception_handler(
    Exception,
    general_exception_handler
)

app.include_router(students_router)


@app.get("/")
def root():
    return {
        "message": "Student Management System API is running"
    }