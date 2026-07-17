import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from Task2_access.permission_manager import PermissionManager

pm = PermissionManager()

stu_session={
    "role": "student",
    "id": "2021-01-001"
}

tea_session={
    "role": "teacher",
    "id": "DIU-FAC-001"
}

print(pm.check(stu_session, {"type":"self"}))
print(pm.check(stu_session, {"type":"student"}))
print(pm.check(stu_session, {"type":"teacher"}))

print(pm.check(tea_session, {"type":"self"}))
print(pm.check(tea_session, {"type":"student"}))
print(pm.check(tea_session, {"type":"teacher"}))