"""
Write a program that allows the user to enter the radius (cm) and height (cm) 
of a cylindrical thermos, 
the program should calculate the volume of the thermos 
and display "True" if the user can fill the thermos with 300 ml of water 
and "False" otherwise
(Remember 1ml = 1cm3)
"""

radius = float (input("Enter the radius >> "))
height = float (input("Enter the height >> "))
pi = 3.14

volume = pi * (radius ** 2) * height

print("The volume of the thermos is >>", volume, "cm3")

condition = volume >= 300
print("Can the user fill the thermos with 300 ml of water? >>", condition)