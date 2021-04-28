from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self):
        this.curr_user = None
        this.password_hash = None

    def set_user(user):
        this.curr_user = user

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class UserManager:
    user_table: str = "users"

    def __init__(self):
        this.__user = User()
