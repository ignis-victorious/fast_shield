"""
🎓 Student Routes

This file contains all the API routes related to students.
For Starters:
- These routes let you create, read, update, and delete students
- Each route handles a different type of request
"""

#
#  Import LIBRARIES
from faker import Faker
from fastapi import APIRouter, HTTPException, Path, Query

from database.mock_db import MockDatabase, get_database

#  Import FILES
from models.student import Student, StudentCreate

#


# Create a router instancy for student-related routes
router: APIRouter = APIRouter(
    prefix="/students",  # ALL routes in this file will start with /students
    tags=["students"],
    # This groups them in the documentation
)


# Create a Faker instance for random student generation
fake: Faker = Faker()


@router.get(path="/", response_model=list[Student])
async def get_all_students() -> list[Student]:
    """
    📚 GET ALL STUDENTS - Returns a list of all students in our school
    For beginners:
    - This is like asking the principal for a list of everyone in the school
    - The response_model tells FastAPI what the response should look like
    """
    db: MockDatabase = get_database()
    return db.students


@router.get(path="/random", response_model=Student)
async def get_random_student() -> Student:
    """
    🎲 GET RANDOM STUDENT - Returns a randomly selected student
    For Starters:
    - This is like picking a name out of a hat!
    - Notice this route comes BEFORE /{student_id} to avoid conflicts
    """
    db: MockDatabase = get_database()
    if not db.students:
        raise HTTPException(status_code=404, detail="No students found in our school! Time to recruit some!")

    random_student: Student = fake.random_element(elements=db.students)
    return random_student


@router.get(path="/search")
async def search_students(
    name: str | None = Query(default=None, description="Search by student name"),
    grade: str | None = Query(default=None, description="Filter by grade level"),
    min_age: int | None = Query(default=None, description="Minimum age", ge=5),
    max_age: int | None = Query(default=None, description="Maximum age", le=18),
) -> tuple[dict[str, dict[str, str | int | None] | int | list[Student]]]:
    """
    🔎 SEARCH STUDENTS - Find students based on different criteria
    For Starters:
    - Query parameters are like filling out a search form
    - You can combine multiple filters (name AND grade AND age, etc.)
    - Example: /students/search?grade=5th&min_age=10
    """

    db: MockDatabase = get_database()
    filtered_students = db.students

    # Filter by name if provided
    if name:
        filtered_students: list[Student] = [s for s in filtered_students if name.lower() in s.name.lower()]

    # Filter by grade if provided
    if grade:
        filtered_students: list[Student] = [s for s in filtered_students if s.grade.lower() == grade.lower()]

    # Filter by minimum age if provided
    if min_age:
        filtered_students: list[Student] = [s for s in filtered_students if s.age >= min_age]
    # Filter by maximum age if provided
    if max_age:
        filtered_students: list[Student] = [s for s in filtered_students if s.age <= max_age]

    return (
        {
            "search_criteria": {"name": name, "grade": grade, "min_age": min_age, "max_age": max_age},
            "total_found": len(filtered_students),
            "students": filtered_students,
        },
    )


@router.get(path="/{student_id}", response_model=Student)
async def get_student(
    student_id: int = Path(default=..., description="The ID of the student you want to find", ge=1),
) -> Student:
    """
    🔎 GET ONE STUDENT - Find a specific student bv their ID number
    For Starters:
    - This is like looking up someone in a phone book using their ID
    - The {student_id) in the URL is called a "path parameter"
    - Path(..., ge=1) means the ID must be 1 or greater
    """

    db: MockDatabase = get_database()
    # Look through all students to find the one with matching ID
    for student in db.students:
        if student.id == student_id:
            return student

    # If we didn't find the student, tell the user with a helpful error message
    raise HTTPException(
        status_code=404,
        detail="Oops! We couldn't find a student with ID {student_id}. Maybe they transferred this student!",
    )


@router.post(path="/", response_model=Student)
async def create_student(student_data: StudentCreate) -> Student:
    """
    ➕ CREATE NEW STUDENT - Add a new student to our school
    For Starters:
    - This is like enrolling a new student
    - We take their information and give them a new student ID number
    - The student information comes in the request body as JSON
    """

    db: MockDatabase = get_database()

    # Create a new student with an auto-generated ID
    new_student: Student = Student(id=db.next_student_id, **student_data.model_dump())

    # Add the student to our database
    db.students.append(new_student)
    db.next_student_id += 1

    return new_student


@router.put(path="/{student_id}", response_model=Student | None)
async def update_student(
    student_id: int = Path(default=..., description="The ID of the student to update"),
    student_data: StudentCreate | None = None,
) -> Student:
    """
    ✏️ UPDATE STUDENT - Modify an existing student's information
    For Starters:
    - This is like updating a student's records when they change grades
    - PUT means "replace all the information with new information"

    """

    db: MockDatabase = get_database()

    # Find the student to update
    for i, student in enumerate(iterable=db.students):
        if student.id == student_id:
            # --- FIX STARTS HERE ---
            # 1. Check if student_data is NOT None before trying to use it.
            if student_data is None:
                # Handle the case where the update data is missing.
                # Since this is a PUT (full replacement), missing data is often an error.
                # For now, we'll assume a successful update means no changes were provided,
                # so we just return the existing student without modification.
                return student

            # 2. If it's not None, Pylance now knows it's a StudentCreate object and calling .model_dump() is safe.
            # Update the student's information
            updated_student: Student = Student(id=student_id, **student_data.model_dump())
            # --- FIX ENDS HERE ---

            # updated_student: Student = Student(id=student_id, **student_data.model_dump())
            db.students[i] = updated_student
            return updated_student

    # If student not found, return an error
    raise HTTPException(
        status_code=404, detail=f"Student with ID {student_id} not found. Cannot update a student who doesn't exist! 🤷"
    )


@router.delete(path="/{student_id}")
async def delete_student(
    student_id: int = Path(default=..., description="The ID of the student to remove"),
) -> dict[str, str | Student]:
    """
    🗑️ DELETE STUDENT - Remove a student from our school system
    For Starters:
    - This is like when a student transfers to another school
    - DELETE removes the student completely from our database
    """

    db: MockDatabase = get_database()

    # Find and remove the student
    for i, student in enumerate(iterable=db.students):
        if student.id == student_id:
            removed_student: Student = db.students.pop(i)
            return {
                "message": f"Student {removed_student.name} has been removed from the school system",
                "removed_student": removed_student,
            }

    # If student not found, return an error
    raise HTTPException(
        status_code=404, detail=f"Student with ID {student_id} not found. Cannot remove a student who doesn't exist"
    )
