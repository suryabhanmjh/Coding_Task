# 7. Simple Interest Calculation

p = float(input("Enter Principal: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (years): "))

si = (p * r * t) / 100
print("Simple Interest =", si)
