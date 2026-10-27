# Attendance Eligibility Checker

## 1. Description

The Attendance Eligibility Checker is a simple Python program that calculates a student's attendance percentage and determines whether the student is eligible to attend examinations based on the minimum attendance requirement of 75%.

The program accepts the number of classes attended and the total number of classes as input. It validates the attendance details, calculates the attendance percentage, and displays the eligibility result.

## 2. Objectives

- To calculate a student's attendance percentage.
- To determine examination eligibility based on attendance.
- To understand conditional statements in Python.
- To validate user inputs.

## 3. Features

- Accepts the number of classes attended and total classes.
- Calculates attendance percentage.
- Checks eligibility based on the 75% attendance requirement.
- Validates attendance details.
- Displays appropriate messages for valid and invalid inputs.

## 4. Technologies Used

- **Programming Language:** Python 3
- **IDE:** PyCharm
- **Concepts:** Input/output statements, arithmetic operators, conditional statements, and input validation.

## 5. How It Works

1. The user enters the number of classes attended.
2. The user enters the total number of classes.
3. The program validates the attendance details.
4. If the details are valid, the program calculates the attendance percentage.
5. It checks whether the attendance percentage is at least 75%.
6. Finally, it displays the eligibility result.

## 6. Algorithm

1. Start.
2. Read the number of classes attended.
3. Read the total number of classes.
4. Check whether the attendance details are valid.
5. If the details are invalid, display "Invalid attendance details!".
6. Otherwise, calculate the attendance percentage using the formula:

   **Attendance Percentage = (Attended Classes / Total Classes) × 100**

7. If the attendance percentage is greater than or equal to 75%, display "Eligible for examinations."
8. Otherwise, display "Not eligible for examinations."
9. Stop.

## 7. Flowchart

The flowchart represents the sequence of steps followed by the Attendance Eligibility Checker.



![Attendance Eligibility Checker Flowchart](flowchart.png)

## 8. Formula Used

**Attendance Percentage = (Number of Classes Attended / Total Number of Classes) × 100**

**Eligibility Criteria:**
- Attendance percentage of 75% or above: Eligible.
- Attendance percentage below 75%: Not eligible.
- Invalid attendance details: Error message displayed.

## 9. Sample Input and Output

### Example 1: Eligible Student

**Input:**
```text
Enter attended classes: 80
Enter total classes: 100
```

**Output:**
```text
Attendance Percentage: 80.0%
Eligible for examinations.
```

### Example 2: Not Eligible Student

**Input:**
```text
Enter attended classes: 60
Enter total classes: 100
```

**Output:**
```text
Attendance Percentage: 60.0%
Not eligible for examinations.
```

### Example 3: Invalid Input

**Input:**
```text
Enter attended classes: 110
Enter total classes: 100
```

**Output:**
```text
Invalid attendance details!
```

## 10. How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project in PyCharm or another Python editor.
4. Open the Python program file.
5. Run the program.
6. Enter the requested attendance details.
7. View the attendance percentage and eligibility result.

## 11. Learning Outcomes

Through this project, I learned:

- How to accept user input in Python.
- How to perform arithmetic calculations.
- How to use `if` and `else` statements.
- How to validate user inputs.
- How to apply programming logic to solve a simple real-world problem.

## 12. Conclusion

The Attendance Eligibility Checker is a beginner-friendly Python project that calculates a student's attendance percentage and determines examination eligibility. This project demonstrates the practical application of input/output statements, arithmetic operations, conditional statements, and input validation. It helped me understand the fundamentals of Python programming and how to use them to solve a real-world problem.

## 13. Author

First-Year B.Tech Student

## 14. License

This project is created for educational purposes.
