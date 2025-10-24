#
#  Import LIBRARIES
from pydantic import BaseModel, Field

#  Import FILES
#


class Subject(BaseModel):
    """
    A model representing a school subject
    For Starters:
    - This defines what information we store about each class/subject
    - Every subject has an ID, name, teacher, and room number
    """
    id: int = Field(..., description="Unique subject ID")
    name: str = Field(..., description="Subject name")
    teacher: str = Field(..., description="Teacher's name")
    room_number: str = Field(..., description="Classroom number")