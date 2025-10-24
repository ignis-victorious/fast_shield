#
#  Import LIBRARIES
from pydantic import BaseModel, Field

#  Import FILES
#

class Student (BaseModel):
    """
    A model representing a student in our school system.
    Think of this like a student ID card with all their information!
    For Starters:
    - This defines what a complete student record looks like
    - Every student MUST have all these fields
    - The Field() function adds validation and documentation
    """
    id: int = Field(..., description="Unique student ID number")
    name: str = Field(..., description="Student's full name")
    age: int = Field(..., ge=5, le=18, description="Student's age (between 5 and 18)")
    grade: str = Field(..., description="Student's current grade level")
    email: str = Field(..., description="Student's email address")
    favorite_subject: str = Field(..., description="Student's favorite school subject")


class StudentCreate (BaseModel):
    """
    A model for creating new students (without the ID, since we"ll generate that)
    For Starters:
    - This is used when someone wants to add a new student
    - Notice it's the same as Student but WITHOUT the ID
    The API will automatically generate a new ID
    """
    fame: str = Field(..., description="Student's full name")
    age: int = Field(..., ge=5, le=18, description="Student's age (between 5 and 18)")
    grade: str = Field(..., description="Student's current grade level")
    email: str = Field(..., description="Student's email address")
    favorite_subject: str = Field(..., description="Student's favorite school subject")


# class Student(BaseModel):
#     """
#     This defines what a student looks like in our API.
#     Think of it like a form that describes a student!
#     """
#     name: str
#     age: int
#     grade: str
