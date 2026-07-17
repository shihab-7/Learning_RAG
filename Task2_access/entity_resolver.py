import re

class EntityResolver:

    def __init__(self):
        self.student_pattern = r"\b\d{4}-\d{2}-\d{3}\b"
        self.teacher_pattern = r"\bDIU-FAC-\d+\b"

    def resolve(self, query):

        student = re.search(self.student_pattern, query)

        if student:
            return {
                "type": "student",
                "id": student.group()
            }
        
        teacher = re.search(self.teacher_pattern, query)
        if teacher:
            return {
                "type": "teacher",
                "id": teacher.group()
            }
        
        return {
            "type": "self",
            "id": None
        }