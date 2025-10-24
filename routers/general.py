#
#  Import LIBRARIES
from fastapi import APIRouter
from datetime import datetime
#  Import FILES
from ..database.mock_db import get_database
#


# Create a router instance - this groups related routes together
router: APIRouter = APIRouter()


@router.get(path="/")
async def read_root() -> dict[str, str | dict[str, str]]:
    """
    🏠 HOME PAGE - This is the first page people see when they visit our API
    For Starters:
    - When someone goes to http://localhost:8000/ they'll see this message
    - This is like the welcome page of our API
    """
    return {
        "message": "Welcome to our FastAPI School System! ",
        "tip": "Visit /docs to see all available endpoints and try them out!",
        "endpoints": {
            "students": "/students - Get all students",
            "subjects": "/subjects - Get all subjects",
            "random_student": "/students/random - Get a random student",
            "documentation": "/docs - Interactive API documentation",
        },
    }





@router.get(path="/stats")
async def get_school_stats():# -> dict[str, str] | dict[str, dict[str, int | float] | Any | str]:# -> dict[str, str] | dict[str, dict[str, int | float] | Any | str]:
    """
    📊 SCHOOL STATISTICS - Get interesting facts about our school
    For Starters:
    - This endpoint shows some fun statistics about our students and subjects
    - It demonstrates how to calculate data from our database
    """

    db = get_database()

    if not db.students:
        return {"message": "No students to analyze! 📊"}

    # Calculate some interesting statistics
    total_students: int = len(db.students)
    ages:list(int) = [student.age for student in db.students]
    average_age: float = sum(ages) / len(ages)

    # Count students by grade
    grade_count = {}
    for student in db.students:
        grade_count[student.grade] = grade_count.get(student.grade, 0) + 1
    
    # Count favorite subjects
    subject_popularity = {}
    for student in db.students:
        subject = student. favorite_subject
        subject_popularity[subject] = subject_popularity.get(subject, 0) + 1
    
    # Find most popular subject
    most_popular_subject = max(subject_popularity, key=subject_popularity.get) if subject_popul
    
    return {
        "school_overview": {
            "total_students": total_students,
            "total_subjects": len(db.subjects),
            "average_student_age": round(number=average_age, 1)
        },
        "grade distribution": grade_count,
        "subject_popularity": subject_popularity,
        "most popular_subject": most_popular_subject,
        "generated_at": datetime.now().isoformat()
    }


@router.get(path="/health") 
async def health_check() -> dict[str, str | int]:
    """
    ❤️ HEALTH CHECK - Make sure our API is working properly
    For beginners:
    - This is like checking if the school's systems are all running smoothly
    - Other services can call this to make sure our API is still working
    """

    db = get_database()

    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "database_status": "connected",
        "total_students": len(db.students),
        "total_subjects": len(db.subjects),
        "message": "All systems are go! 🚀"
    }
