from access_control.decider import AccessControlDecider
from access_control.permissions import PermissionManager
from access_control.data_manager import DataManager


class QueryManager:

    def __init__(self, retriever, llm):

        self.query_type=AccessControlDecider()
        self.permission_manager=PermissionManager()
        self.data_manager=DataManager()
        self.retriever=retriever
        self.llm=llm

    def format_student(self, student):
        return f"""
            Student Information

            Student ID : {student['Student ID']}
            Name : {student['Student Name']}
            Department : {student['Department']}
            Program : {student['Program']}
            Current Semester : {student['Current Semester']}
            CGPA : {student['CGPA']}
            Advisor : {student['Advisor']}
            Tuition Status : {student['Tuition Status']}
            Scholarship Status : {student['Scholarship Status']}
            Attendance : {student['Attendance %']}
            Email : {student['Email']}
            Phone : {student['Phone']} """
    
    def format_teacher(self, teacher):
        return f"""
                Teacher Information

                Faculty ID : {teacher['Faculty ID']}
                Name : {teacher['Name']}
                Department : {teacher['Department']}
                Designation : {teacher['Designation']}
                Courses Taught : {teacher['Courses Taught']}
                Office Room : {teacher['Office Room']}
                Office Hours : {teacher['Office Hours']}
                Research Interests : {teacher['Research Interests']}
                Email : {teacher['Email']} """

    def process_query(self,session,query):

        type = self.query_type.decide_access(query)
        print(f"Query Type: {type}")
        # print(session)

        if type == "PERSONAL":
            if session["role"]=="student":
                return self.format_student(session["profile"])
            else :
                return self.format_teacher(session["profile"])
        
        elif type == "UNIVERSITY":
            docs = self.retriever.search(query)
            context = "\n\n".join(doc.page_content for doc in docs)
            answer = self.llm.ask(query, context)

            return answer
        
        elif type == "MIXED":
            if session["role"]=="student":
                personal_context = self.format_student(session["profile"])

            else:
                personal_context = self.format_teacher(session["profile"])
            
            docs = self.retriever.search(query)
            rag_context = "\n\n".join(doc.page_content for doc in docs)

            final_context = f"""
                    PERSONAL INFORMATION :

                    {personal_context}

                    UNIVERSITY INFORMATION :

                    {rag_context}"""
            
            answer = self.llm.ask(query, final_context)
            return answer
        return "Invalid query type."