from access_control.data_manager import DataManager

class Auth:

    def __init__(self):
        self.data_manager = DataManager()

    
    def student_login(self,student_id, password):

        student = self.data_manager.get_student_info(student_id)
        pswd = "123"
        if student is None:
            return None
        
        if password == pswd and self.data_manager.student_exists(student_id):
            return {
                "role": "student",
                "id": student_id,
                "profile":student
            }
        
    def teacher_login(self,teacher_id, password):
        teacher = self.data_manager.get_teacher_info(teacher_id)
        pswd = "abc"
        if teacher is None:
            return None
        
        if password == pswd and self.data_manager.teacher_exists(teacher_id):
            return {
                "role": "teacher",
                "id": teacher_id,
                "profile":teacher
            }
    
    def login(self):

        print("\n============Login============")
        print("1. Student Login")
        print("2. Teacher Login")

        choice = input("\nEnter your role (1 or 2): ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            password = input("Enter Password: ")
            session = self.student_login(student_id, password)
            if session:
                print("\nLogin successful!")
                return session
            else:
                print("\nInvalid Student ID or Password.")
                return None

        elif choice == "2":
            teacher_id = input("Enter Teacher ID: ")
            password = input("Enter Password: ")
            session = self.teacher_login(teacher_id, password)
            if session:
                print("\nLogin successful!")
                return session
            else:
                print("\nInvalid Teacher ID or Password.")
                return None
        else:
            print("\nInvalid choice.")
            return None
        
        if session is None:
            print("\nLogin failed. Please try again.")
            return None
        
        print(f"\nWelcome {session['profile'].get('Student Name' if session['role'] == 'student' else 'Name')}!")
        return session