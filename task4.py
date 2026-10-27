
# Task 4: Password Creation

password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True
    if ch in "@#$!%*":
        has_special = True

score = 0

if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

if "123" in password or "password" in password.lower():
    print("Fail - Avoid easy passwords!")
elif len(password) < 8:
    print("Fail - Weak - Password must have at least 8 characters.")
else:
    print(f"Score: {score}/5")

    if score <= 2:
        print("Result: WEAK Password")
    elif score <= 4:
        print("Result: MEDIUM Password")
    else:
        print("Result: STRONG Password - Super!")
