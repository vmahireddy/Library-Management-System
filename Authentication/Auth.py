from Database import db
class Auth:
    def __init__(self):
        db.connect()
    def signup(self, username, password):
        if not username or not password:
            print("Username and password cannot be empty.")
            return False
        user = db.fetch_query("SELECT * FROM users WHERE username = ?", (username,))
        if user:
            print("Username already exists.")
            return False
        db.execute_query("INSERT INTO users (username, password) VALUES (?, ?)",(username, password))
        print("Signup successful.")
        return True
    def login(self, username, password):
        if not username or not password:
            print("Username and password cannot be empty.")
            return False
        user = db.fetch_query("SELECT * FROM users WHERE username = ? AND password = ?",
                (username, password))
        if user:
            print("Login successful.")
            return True
        else:
            print("Invalid username or password.")
            return False