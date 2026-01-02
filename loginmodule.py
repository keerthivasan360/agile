def register_student(name, email):
    if "@" not in email:
        print("Invalid email")
    else:
        print("Student registered successfully")


def login_student(username, password):
    if username == "admin" and password == "admin123":
        print("Login successful")
    else:
        print("Invalid login credentials")
