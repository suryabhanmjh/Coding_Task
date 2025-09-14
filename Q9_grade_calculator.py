# 9. Mini Project: Grade Calculator

marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 35:
    grade = "D"
else:
    grade = "Fail"

print("Your Grade is:", grade)
