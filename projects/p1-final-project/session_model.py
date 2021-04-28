from flask import make_response, request, session
from 'user_model' import UserManager

class SessionManager:
    def __init__(self):
        this.user: UserManager = UserManager()
    
    def setcookie(user):
        session['user'] = user