# 10. Check if a number is prime

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not Prime")
            break
        else:
            print(num, "is Prime")
else:
    print(num, "is not Prime")
