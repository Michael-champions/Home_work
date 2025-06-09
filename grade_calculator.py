
# Grade Calculator Program
# This program calculates the letter grade based on a numeric score input by the user.
score = int(input("Enter your numeric grade (0-100): "))

# Determine the base letter grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Determine the sign (+, -, or none)
sign = ""

# Only add signs for grades B, C, and D (not A or F)
if grade in ["B", "C", "D"]:
    last_digit = score % 10
    if last_digit >= 7:
        sign = "+"
    elif last_digit < 3:
        sign = "-"

# Print the final letter grade
print(f"Your grade is: {grade}{sign}")

# Check if the student passed (passing is 70 or above)

if score >= 70:
    print("Congratulations, you passed the course!")
else:
    print("Sorry, you did not pass the course.")

