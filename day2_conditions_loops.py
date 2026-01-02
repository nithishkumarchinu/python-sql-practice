# Day 2 - Conditions and Loops

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)
