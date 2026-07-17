from Task2_access.entity_resolver import EntityResolver
from Task2_access.permission_manager import PermissionManager
from Task2_access.data_manager import DataManager

class QueryManager:

    def __init__(self, retriever, llm):

        self.entity_resolver = EntityResolver()
        self.permission_manager = PermissionManager()
        self.data_manager = DataManager()
        self.retriever = retriever
        self.llm = llm

    
    def _student_context(self, student):

        return f"""
                Student Information

                Student ID: {student['Student ID']}
                Name: {student['Student Name']}
                Department: {student['Department']}
                Program: {student['Program']}
                Current Semester: {student['Current Semester']}
                CGPA: {student['CGPA']}
                Advisor: {student['Advisor']}
                Tuition Status: {student['Tuition Status']}
                Scholarship Status: {student['Scholarship Status']}
                Attendance: {student['Attendance %']}
                Email: {student['Email']}
                Phone: {student['Phone']}
                """
    
    def _teacher_context(self, teacher):
        return f"""
                Teacher Information

                Faculty ID: {teacher['Faculty ID']}
                Name: {teacher['Name']}
                Department: {teacher['Department']}
                Designation: {teacher['Designation']}
                Courses Taught: {teacher['Courses Taught']}
                Office Room: {teacher['Office Room']}
                Office Hours: {teacher['Office Hours']}
                Research Interests: {teacher['Research Interests']}
                Email: {teacher['Email']}
                """
    
    def process_query(self, session, query):

        docs = self.retriever.search(query)
        rag_context = "\n\n".join(doc.page_content for doc in docs)

        entity = self.entity_resolver.resolve(query)

        if not self.permission_manager.check(session, entity):
            return {
                "answer": "দুঃখিত, আপনি এই তথ্য দেখার অনুমতি পান না।",
                "sources": docs
            }
        
        personal_context=""

        if entity["type"]=="self":
            if session["role"]=="student":
                personal_context=self._student_context(session["profile"])
            else :
                personal_context=self._teacher_context(session["profile"])

        elif entity["type"]=="student":
            student = self.data_manager.get_student_info(entity["id"])

            if student is None:
                return {
                    "answer": "Student not found.",
                    "sources": docs
                }
            personal_context=self._student_context(student)

        elif entity["type"]=="teacher":
            teacher = self.data_manager.get_teacher_info(entity["id"])

            if teacher is None:
                return {
                    "answer": "Teacher not found.",
                    "sources": docs
                }
            personal_context=self._teacher_context(teacher)

        final_context = f"""
            PERSONAL INFORMATION

            {personal_context}

            UNIVERSITY INFORMATION

            {rag_context}
        """
        answer = self.llm.ask(query, final_context)

        return {
            "answer": answer,
            "sources": docs
        }