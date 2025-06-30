from datetime import datetime

class Course:
    """Represents a university course."""
    def __init__(self, course_id: int, title: str, credits: int):
        self.course_id = course_id
        self.title = title
        self.credits = credits

    def get_info(self) -> str:
        """Returns a string containing course information."""
        return f"{self.title} ({self.course_id}) - {self.credits} credits"


class Registration:
    """Handles the student-course registration process."""
    def __init__(self, reg_id: int, student, course: Course):
        self.reg_id = reg_id
        self.student = student            # Association
        self.course = course              # Aggregation
        self.reg_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def submit(self) -> bool:
        """Submits the registration request."""
        print(f"Registration ID: {self.reg_id}")
        print(f"Student: {self.student.name} registered for {self.course.get_info()} on {self.reg_date}")
        return True


class Student:
    """Represents a student who can register for courses."""
    def __init__(self, student_id: int, name: str, email: str):
        self.student_id = student_id
        self.name = name
        self.email = email

    def register(self, course: Course):
        """Creates and submits a course registration."""
        registration = Registration(reg_id=1001, student=self, course=course)
        print(f"{self.name} is registering for a course...")
        registration.submit()


# --- Simulate Scenario ---
if __name__ == "__main__":
    # Create a course
    python_course = Course(course_id=101, title="Intro to Software Engineering", credits=3)

    # Create a student
    student_olajumoke = Student(student_id=1, name="Olajumoke Toriola", email="S282238@UOS.AC.UK")

    # Student registers for a course
    student_olajumoke.register(python_course)
