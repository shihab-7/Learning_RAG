import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from access_control.permissions import PermissionManager

pm = PermissionManager()

student_session = {
    "role": "student",
    "id": "2024-11-001"
}

teacher_session = {
    "role": "teacher",
    "id": "DIU-FAC-101"
}

# student nijer session diye nijer details access korte parbe
print(pm.can_access_student(student_session, "2024-11-001"))

# student nijer session diye onno students er details access korte parbe na
print(pm.can_access_student(student_session, "2024-11-002"))

# student nijer session diye teacher er details access korte parbe na karon ei functionality rakhai nai
# print(pm.can_access_teacher(student_session,"DIU-FAC-101"))

# teacher nijer session diye student er details access korte parbe na
print(pm.can_access_student(teacher_session,"2024-11-001"))

# teacher student er session access korte parbe na
print(pm.can_access_teacher(student_session))

# teacher teacher er session access korte parbe
print(pm.can_access_teacher(teacher_session))