from datetime import datetime

class Registration:
    """Handles the student-course registration process."""
    def __init__(self, reg_id: int, student, course):
        self.reg_id = reg_id
        self.student = student            # Association
        self.course = course              # Aggregation
        self.reg_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def submit(self) -> bool:
        """Submits the registration request."""
        print(f"Registration ID: {self.reg_id}")
        print(f"Student: {self.student.name} registered for {self.course.get_info()} on {self.reg_date}")
        return True
