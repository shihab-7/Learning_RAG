import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from access_control.decider import AccessControlDecider

decide = AccessControlDecider()

print(decide.decide_access("What is my CGPA and what scholarship can I apply for?"))

print(decide.decide_access("আমার সিজিপিএ কত এবং স্কলারশিপের নিয়ম কী?"))

print(decide.decide_access("লাইব্রেরির নিয়ম কী?"))

