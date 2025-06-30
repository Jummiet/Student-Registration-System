from course import Course
from student import Student

# --- Simulate Scenario ---
if __name__ == "__main__":
    # Create a course
    python_course = Course(course_id=101, title="Intro to Software Engineering", credits=5)

    # Create a student
    student_olajumoke = Student(student_id=1, name="Olajumoke Toriola", email="S282238@UOS.AC.UK")

    # Student registers for a course
    student_olajumoke.register(python_course)
