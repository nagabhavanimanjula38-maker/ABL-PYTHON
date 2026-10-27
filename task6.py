
# Task 6: Student Email Validation

email = input("Enter student email: ")

if email.count("@") == 1:
    parts = email.split("@")

    if parts[0] != "" and "." in parts[1]:
        if not parts[1].startswith(".") and not parts[1].endswith("."):
            print("Valid email format")
        else:
            print("Invalid email format")
    else:
        print("Invalid email format")
else:
    print("Invalid email format")
