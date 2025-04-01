class UserAuthentication:
    def login(self):
        pass

class EmailAuth(UserAuthentication):
    def login(self):
        return "Email/password authentication"

class GoogleAuth(UserAuthentication):
    def login(self):
        return "Google authentication"

class FingerprintAuth(UserAuthentication):
    def login(self):
        return "Fingerprint authentication"

logins = [UserAuthentication(), EmailAuth(), GoogleAuth(), FingerprintAuth()]

for login in logins:
    print(login.login())