import pandas as pd
from pathlib import Path

class DataManager:

    def __init__(self, student_data=None, teacher_data=None):
        project_root = Path(__file__).resolve().parent.parent
        student_data = student_data or project_root / "informations" / "students_data.csv"
        teacher_data = teacher_data or project_root / "informations" / "teachers_data.csv"

        self.students = pd.read_csv(student_data)
        self.teachers = pd.read_csv(teacher_data)

    
    def get_student_info(self, student_id):
        student = self.students[self.students['Student ID'] == student_id]
        if student.empty:
            return None

        return student.iloc[0].to_dict()
    
    def get_teacher_info(self, teacher_id):
        teacher = self.teachers[self.teachers['Faculty ID'] == teacher_id]
        if teacher.empty:
            return None

        return teacher.iloc[0].to_dict()
    
    def student_exists(self, student_id):
        return self.get_student_info(student_id) is not None
    
    def teacher_exists(self, teacher_id):
        return self.get_teacher_info(teacher_id) is not None
