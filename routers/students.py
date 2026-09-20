from typing import Optional
from exceptions import StudentNotFoundException
from fastapi import APIRouter, Query

from schemas.student import (
    StudentCreate,
    StudentUpdate,
    StudentPatch,
    StudentOut,
)
from services import student_service


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post(
    "",
    response_model=StudentOut,
    status_code=201
)
def create_student(student: StudentCreate):
    return student_service.create_student(student)


@router.get(
    "",
    response_model=list[StudentOut]
)
def get_students(
    department: Optional[str] = Query(default=None),
    min_age: Optional[int] = Query(default=None, gt=0),
    max_age: Optional[int] = Query(default=None, lt=100)
):
    students = student_service.get_all_students()

    if department:
        students = [
            student
            for student in students
            if student["department"] == department
        ]

    if min_age is not None:
        students = [
            student
            for student in students
            if student["age"] >= min_age
        ]

    if max_age is not None:
        students = [
            student
            for student in students
            if student["age"] <= max_age
        ]

    return students


@router.get(
    "/{student_id}",
    response_model=StudentOut
)
def get_student(student_id: int):
    student = student_service.get_student(student_id)

    if student is None:
        raise StudentNotFoundException(student_id)

    return student


@router.put(
    "/{student_id}",
    response_model=StudentOut
)
def update_student(
    student_id: int,
    student: StudentUpdate
):
    updated_student = student_service.update_student(
        student_id,
        student
    )

    if updated_student is None:
        raise StudentNotFoundException(student_id)

    return updated_student


@router.patch(
    "/{student_id}",
    response_model=StudentOut
)
def patch_student(
    student_id: int,
    student: StudentPatch
):
    updated_student = student_service.patch_student(
        student_id,
        student
    )

    if updated_student is None:
        raise StudentNotFoundException(student_id)

    return updated_student


@router.delete(
    "/{student_id}",
    status_code=204
)
def delete_student(student_id: int):
    deleted = student_service.delete_student(student_id)

    if not deleted:
        raise StudentNotFoundException(student_id)