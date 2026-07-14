class PermissionManager:

    def can_access_student(self, session, req_stu_id):

        if session["role"]=="teacher":
            return True
        
        if session["role"]=="student":
            return session["id"]==req_stu_id
        
        return False

    def can_access_teacher(self, session):
        return session["role"]=="teacher"