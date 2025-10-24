#
#  Import LIBRARIES
from fastapi import APIRouter, HTTPException, Path  # , Query

from database.mock_db import MockDatabase, get_database

#  Import FILES
from models.subject import Subject

#


# Create a router instancy for student-related routes
router: APIRouter = APIRouter(
    prefix="/subjects",  # ALL routes in this file will start with /students
    tags=["subjects"],
    # This groups them in the documentation
)


@router.get(path="/", response_model=list[Subject])
async def get_all_subjects() -> list[Subject]:
    """
    📖 GET ALL SUBJECTS - Returns a list of all school subjects
    For beginners:
    - This shows all the classes available in our school
    - Similar to getting all students, but for subjects
    """

    db: MockDatabase = get_database()
    return db.subjects


@router.get(path="/{subject_id}", response_model=Subject)
async def get_subject(subject_id: int = Path(default=..., description="The ID of the subject you want to find")):
    """
    📝 GET ONE SUBJECT - Find a specific subject by its ID
    For beginners:
    - This is like looking up information about a specific class
    - Uses the same pattern as getting a single student
    """

    db: MockDatabase = get_database()

    for subject in db.subjects:
        if subject.id == subject_id:
            return subject

    raise HTTPException(
        status_code=404, detail=f"Subject with ID {subject_id} not found. Maybe it's not offered this semester"
    )
