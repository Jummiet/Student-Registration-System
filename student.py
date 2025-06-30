from registration import Registration

class Student:
    """Represents a student who can register for courses."""
    def __init__(self, student_id: int, name: str, email: str):
        self.student_id = student_id
        self.name = name
        self.email = email

    def register(self, course):
        """Creates and submits a course registration."""
        registration = Registration(reg_id=1001, student=self, course=course)
        print(f"{self.name} is registering for a course...")
        registration.submit()
