from course import Course
from student import Student

# --- Simulate Scenario ---
if __name__ == "__main__":
    # Create a course
    python_course = Course(course_id=UMDCOM202-92022, title="Intro to Software Engineering", credits=5)

    # Create a student
    student_olajumoke = Student(student_id=6891110, name="Olajumoke Toriola", email="S28223800@UOS.AC.UK")

    # Student registers for a course
    student_olajumoke.register(python_course)
