"""
Write a program that allows the input of two numbers
and displays "True" if the first number is divisible by the second,
"False" if not
"""

num1 = int (input("Introduce first number >> "))
num2 = int (input("Introduce second number >> "))
result = num1 % num2
condition = result == 0

print("Is", num1, "divisible by", num2, "? >>", condition)