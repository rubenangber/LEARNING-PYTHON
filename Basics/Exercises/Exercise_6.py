"""
Write a program that generates a business email from the input of the following data:
business website (assume that it starts with www. and ends with .com)
    First name
    Second name
    Surname
    Year of birth

The email will have to have the following structure:
    First letter of first name
    First letter of middle name
    Surname
    Last two numbers of the year of birth
    @
    Company name
    .com
"""

url = input("Insert company name >> ")
first_name = input("Insert first name >> ")
second_name = input("Insert second name >> ")
surname = input("Insert surname >> ")
year = int (input("Insert year >> "))

print("{}{}{}{}@{}.com".format(first_name[0], second_name[0], surname, str(year)[2:], url))
