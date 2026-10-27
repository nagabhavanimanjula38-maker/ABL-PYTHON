# Student Marks Analysis

print("Student Marks Analysis")

m1 = int(input("Enter marks in subject 1 (0-100): "))
m2 = int(input("Enter marks in subject 2 (0-100): "))
m3 = int(input("Enter marks in subject 3 (0-100): "))

if (m1 < 0 or m1 > 100 or
    m2 < 0 or m2 > 100 or
    m3 < 0 or m3 > 100):
    print("Invalid marks! Enter marks between 0 and 100.")
else:
    average = (m1 + m2 + m3) / 3

    print("Average marks:", round(average, 2))

    if m1 >= 40 and m2 >= 40 and m3 >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")
        