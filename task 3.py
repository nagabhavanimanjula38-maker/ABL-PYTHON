
# Attendance Eligibility

attended = int(input("Enter attended classes: "))
total = int(input("Enter total classes: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details!")
else:
    percent = (attended / total) * 100

    if percent >= 75:
        print("Eligible -", round(percent, 2), "%")
    else:
        print("Not Eligible -", round(percent, 2), "%")
        print("You have to attend more classes.")
