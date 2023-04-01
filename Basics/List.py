list = ["First" , "Second" ,  "Third"]
#          0         1           2

element_1 = list[0]
print(element_1)

print(list[0 : 2])

list[0] = "Ruben"
list[1] = "Angoso"
list[2] = "Berrocal"
print(list)

newList = [True, 2, "Alex"] + ["Beatriz", 8]
print(newList)

newList = ["Alex", "Beatriz"] * 3
print(newList)

condition_1 = "Alex" in newList
print(condition_1)
condition_2 = "Ruben" in newList
print(condition_2)