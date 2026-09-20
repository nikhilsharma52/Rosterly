from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal


Department = Literal["CSE", "ECE", "MECH", "CIVIL"]


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=100)
    email: EmailStr
    department: Department
    marks: Optional[float] = Field(default=None, ge=0, le=100)


class StudentUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=100)
    email: EmailStr
    department: Department
    marks: Optional[float] = Field(default=None, ge=0, le=100)


class StudentPatch(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=50)
    age: Optional[int] = Field(default=None, gt=0, lt=100)
    email: Optional[EmailStr] = None
    department: Optional[Department] = None
    marks: Optional[float] = Field(default=None, ge=0, le=100)


class StudentOut(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    department: Department
    marks: Optional[float] = None