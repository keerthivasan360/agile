def register_student(name, email):
    if "@" not in email:
        print("Invalid email")
    else:
        print("Student Registered Successfully")
