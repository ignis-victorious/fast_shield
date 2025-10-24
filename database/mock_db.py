
#
#  Import LIBRARIES
from faker import Faker
#  Import FILES
from models.student import Student
from models.subject import Subject
#


# Create a Faker instance to generate fake data
fake: Faker = Faker()

class MockDatabase:
    """
    A simple mock database that stores data in memory.
    For Starters:
    - This class acts like a database but simpler
    - It stores students and subjects in Python lists
    - It automatically creates some fake data when it starts
    """

    def __init__ (self):
        """Set up the database with empty lists and starting ID numbers"""
        self.students = []
        self.subjects= []
        self.next_student_id = 1
        self.next_subject_id = 1
        
        # Let's create some fake students and subjects when our database starts up
        self._create_sample_data()


    def _create_sample_data(self) -> None:
        """
        Create some sample students and subjects using Faker

        For Starters:
        - Faker is a library that creates realistic fake data
        - This gives us some data to work with right away
        - In a real app, real users would add this data
        """
        # Create 5 fake students
        for _ in range (5):
            student = Student(
                id=self.next_student_id, 
                name=fake. name (), 
                age=fake.random_int(min=5, max=18),
                grade=fake.random_element(elements=(
                    "Kindergarten", "1st", "2nd", "3rd","4th", "5th","6th", "7th", "8th","9th", "10th", "11th","12th"
                    )), 
                    email=fake.email(),
                    favorite_subject=fake.random_element (elements=(
                        "Math", "Science", "English", "History", "Art", "Music", "PE"
                    ))
            )
            self.students. append(student)
            self.next_student_id += 1

        # Create some school subjects
        subjects_data = [
            {"name": "Matthematics", "teacher": fake.name(), "room_number": "101"}, 
            {"name": "Science", "teacher": fake.name(), "room_number": "102"}, 
            {"name": "English", "teacher": fake.name(), "room_number": "103"},
            {"name": "History", "teacher": fake.name(), "room_number": "104"},
            {"name": "Art", "teacher": fake.name(), "room_number": "105"},
        ]

        for subject_data in subjects_data:
            subject = Subject(id=self.next_subject_id,**subject_data)
            self.subjects.append(subject)
            self. next_subject_id += 1



# Create a single database instance that the whole app will use
_database = MockDatabase()


def get_database() -> MockDatabase:
    """
    Get the database instance
    For beginners: TAB to jump here
    - This function returns our database
    - Using a function makes it easy to change how we get the database later
    - This is called "dependency injection" - a fancy term for "get what you need from somewher
    """
    return _database