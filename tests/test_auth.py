import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from access_control.auth import Auth

auth = Auth()
session = auth.login()
print(session)