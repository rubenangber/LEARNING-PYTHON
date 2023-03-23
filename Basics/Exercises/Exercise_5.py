"""
Write a program that allows the user to input the measures 
of the catheter a and b of a right triangle. 
The program should calculate the hypotenuse 
and display the result with 3 decimal places.
"""

catheter_a = float (input("Introduce a catheter >> "))
catheter_b = float (input("Introduce b catheter >> "))
hypotenuse = ((catheter_a ** 2) + (catheter_b ** 2)) ** (1/2)

print("The hypotenuse is >> {:.3f}".format(hypotenuse))