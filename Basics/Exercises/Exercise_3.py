"""
Create a program that allows you to input a number.
It should show "True" if it is not between 10 and 100 (not including them) 
and "False" otherwise
"""

num1 = int (input("Introduce a number >> "))
condition = num1 <= 10 or num1 >= 100

print(num1, "isn't between 10 and 100? >>", condition)