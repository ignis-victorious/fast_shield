#
#  Import LIBRARIES
from pydantic import BaseModel

#  Import FILES
#


class Student(BaseModel):
    """
    This defines what a student looks like in our API.
    Think of it like a form that describes a student!
    """

    name: str
    age: int
    grade: str
