import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from rag.vectorDB import VectorDatabase
from rag.retrieval_pipeline import Retriever
from rag.llm import UniversityLLM
from Task2_access.query_manager import QueryManager


vector_db = VectorDatabase()
vector_db.load_vector_db()
retriever = Retriever(vector_db)
llm = UniversityLLM()
query_manager = QueryManager(
    retriever=retriever,
    llm=llm
)


student_session = {
    "role": "student",
    "id": "2024-11-001",
    "profile": {
        "Student ID": "2024-11-001",
        "Student Name": "Aahil Rahman",
        "Department": "CSE",
        "Program": "B.Sc. CSE",
        "Current Semester": "Spring 2026",
        "CGPA": 3.82,
        "Advisor": "Dr. M. A. Razzaque",
        "Tuition Status": "Paid",
        "Scholarship Status": "20% SGPA Waiver",
        "Email": "aahil.cse@diu.ac",
        "Phone": "01711-098765",
        "Attendance %": "92%"
    }
}


teacher_session = {
    "role": "teacher",
    "id": "DIU-FAC-101",
    "profile": {
        "Faculty ID": "DIU-FAC-101",
        "Name": "Dr. M. A. Razzaque",
        "Department": "CSE",
        "Designation": "Professor",
        "Courses Taught": "CSE-411, CSE-423",
        "Office Room": "Room-502",
        "Office Hours": "Sun-Tue 10AM-12PM",
        "Research Interests": "AI, Computer Vision",
        "Email": "razzaque@diu.ac"
    }
}


tests = [

    ("Student Self", student_session, "What is my CGPA?"),

    ("Student -> Student", student_session,
     "Show student 2024-11-002"),

    ("Student -> Teacher", student_session,
     "Show teacher DIU-FAC-101"),

    ("Teacher Self", teacher_session,
     "What courses do I teach?"),

    ("Teacher -> Student", teacher_session,
     "Show student 2024-11-001"),

    ("Teacher -> Teacher", teacher_session,
     "Show teacher DIU-FAC-102"),

    ("University", student_session,
     "What is the scholarship policy?"),

    ("Mixed", student_session,
     "Am I eligible for scholarship?")
]


for title, session, query in tests:

    print("=" * 100)
    print(title)
    print("Query :", query)
    print("-" * 100)

    result = query_manager.process_query(
        session=session,
        query=query
    )

    print(result)
    print()