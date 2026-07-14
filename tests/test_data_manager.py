import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from access_control.data_manager import DataManager

dm = DataManager()
print(dm.student_exists("2024-11-001"))
print(dm.get_student_info("2024-11-001"))
print(dm.teacher_exists("DIU-FAC-101"))
print(dm.get_teacher_info("DIU-FAC-101"))
