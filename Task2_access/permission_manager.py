class PermissionManager:

    def check(self, session, entity):

        # teacher student jei login thakbe shei nijer info visit korar access pabe nahoy pabe na
        if entity["type"]=="self":
            return True
        
        # user chay student info teacher hoile pabe nahoy pabe na
        if entity["type"]=="student":
            if session["role"]=="teacher":
                return True
            return False
        
        # user chay teacher info & teacher arek teacher er info dekhte parbe but student teacher er info dekhte parbe na
        if entity["type"]=="teacher":
            if session["role"]=="teacher":
                return True
            return False
        
        return False