# Task 3: Attendance Eligibility

## Description
This Python program checks whether a student is eligible to attend examinations based on their attendance percentage. Students with 75% or more attendance are considered eligible.

## Problem Statement
Develop a Python program to calculate a student's attendance percentage and determine whether the student is eligible based on the minimum attendance requirement of 75%.

## Objectives
- To understand conditional statements in Python.
- To calculate attendance percentage.
- To check eligibility based on attendance.
- To validate attendance details.

## Assumptions
- The total number of classes must be greater than zero.
- The number of attended classes cannot be negative.
- The number of attended classes cannot exceed the total number of classes.
- A student needs at least 75% attendance to be eligible.

## Algorithm
1. Start.
2. Read the number of attended classes.
3. Read the total number of classes.
4. Check whether the attendance details are valid.
5. If the details are invalid, display "Invalid attendance details!".
6. Otherwise, calculate the attendance percentage.
7. If the percentage is 75% or more, display "Eligible" and the percentage.
8. Otherwise, display "Not Eligible", the percentage, and a message to attend more classes.
9. Stop.

## Flowchart
<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/28620230-577d-404a-80f3-1995bf0fba25" />


## Flowchart
Upload your hand-drawn attendance eligibility flowchart here.

## Pseudocode
```text
START
INPUT attended
INPUT total

IF total <= 0 OR attended < 0 OR attended > total
    PRINT "Invalid attendance details!"
ELSE
    percent = (attended / total) * 100

    IF percent >= 75
        PRINT "Eligible -", percent, "%"
    ELSE
        PRINT "Not Eligible -", percent, "%"
        PRINT "You have to attend more classes."
    END IF
END IF

STOP
```

## Test Cases

| Attended Classes | Total Classes | Expected Output |
|---:|---:|---|
| 80 | 100 | Eligible - 80.0 % |
| 60 | 100 | Not Eligible - 60.0 % |
| 75 | 100 | Eligible - 75.0 % |
| 0 | 0 | Invalid attendance details! |
| 110 | 100 | Invalid attendance details! |

## Conclusion
This program demonstrates the use of variables, arithmetic operations, and conditional statements to calculate attendance percentage and determine student eligibility.
