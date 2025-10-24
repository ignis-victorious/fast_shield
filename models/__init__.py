#
#  Import LIBRARIES
from .student import Student, StudentCreate
from .subject import Subject

#  Import FILES
#


# This makes it easy to import models like: from models import Student
__all__: list[str] = ["Student", "StudentCreate", "Subject"]
