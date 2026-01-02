# Day 3 - Functions Practice

def greet():
    print("Welcome to Python programming")

for i in range(3):
    greet()


def add(a, b):
    return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum:", add(x, y))


def max_of_two(a, b):
    return a if a > b else b

print("Larger number:", max_of_two(x, y))


def is_even(n):
    return n % 2 == 0

num = int(input("Enter a number: "))
if is_even(num):
    print("Even number")
else:
    print("Odd number")


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter number for factorial: "))
print("Factorial:", factorial(n))
