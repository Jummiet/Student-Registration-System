class Course:
    """Represents a university course."""
    def __init__(self, course_id: int, title: str, credits: int):
        self.course_id = course_id
        self.title = title
        self.credits = credits

    def get_info(self) -> str:
        """Returns a string containing course information."""
        return f"{self.title} ({self.course_id}) - {self.credits} credits"
