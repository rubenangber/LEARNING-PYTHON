"""
Concatenate
str + str
"""
result = "This" + " is" + " my" + " home"
print(result)

"""
Multiply
str * int
"""
result = "Home" * 3
print(result)

"""
Operator in
"""
result = "coffee" in "A cup of coffee"
print(result)
result = "o" in "coffee"
print(result)

"""
Comparison
"""
result = "egg" == "Egg"
print(result)
result = "Egg" == "Egg"
print(result)
result = "egg" != "Egg"
print(result)
result = "Egg" != "Egg"
print(result)

"""
Python order:
ABCDEFGHI...abcdefghi...
Where A is lower than a
"""
result = "Home" > "Egg"
print(result)
result = "Egg" > "Home"
print(result)

"""
Quotes
"""
result = "This is how you put \"quotes\""
print(result)

"""
Tab
"""
result = "This\tis\thow\tyou\tput\ta\ttab"
print(result)

"""
Length of a string
"""
lenght =len("I am a coffee lover")
print(lenght)

"""
Replace
"""
text = "I like coffee"
newtext = text.replace("coffee","chips") #You can concatenate replaces
print(newtext)                           #text.replace("","").replace("","")...

"""
Stript
To delete at the beginning and at the end
"""
name = " Rube n\t"
finalName = name.strip()    #Spaces, enters and tabs
print(finalName)

surname = "--Ango-so-"
finalSurname = surname.strip("-")
print(finalSurname)

"""
Change upper case and lower case
"""
name = "RUbeN"
print(name.lower())
print(name.upper())
print(name.title())

"""
Start - End
"""
web = "https://github.com/rubenangber/LEARNING-PYTHON"
condition_1 = web.startswith("https:")
print(condition_1)
condition_2 = web.endswith("PYTHON")
print(condition_2)

"""
Find a position in a string
"""
string = "Ruben Angoso|Computer engineer"
position = string.index("|")    #If it doesn't exist, error
print(position)
position = string.find("|")     #If it doesn't exist, returns -1
print(position)

string = "Ruben Angoso|Computer engineer|20"
position1 = string.index("|")
position2 = string.index("|", position1+1)
print(position2)

"""
Is...
"""
string = "12"
condition = string.isdigit()
print(condition)
string = "-12"
condition = string.isdigit()    #ONLY digit
print(condition)

string = "Hello world"
condition = string.isalpha()    #Verify if it only contains letters
print(condition)                #False because it has a space

string = "hello world"
condition = string.islower()
print(condition)

string = "HELLO WORLD"
condition = string.isupper()
print(condition)