from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException


class StudentNotFoundException(Exception):
    def __init__(self, student_id: int):
        self.student_id = student_id


async def student_not_found_handler(
    request: Request,
    exc: StudentNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "error": True,
            "message": f"Student with ID {exc.student_id} not found"
        }
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content={
            "error": True,
            "message": "Validation error",
            "details": exc.errors()
        }
    )


async def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "message": str(exc.detail)
        }
    )


async def general_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "error": True,
            "message": "Internal server error"
        }
    )