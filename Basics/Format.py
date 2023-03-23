name = "Ruben"
age = 20

print("My name is {} and I have {} years".format(name, age))

height = 1.7392
# It rounds
print("My height is {:.3}".format(height))

product = "Expresso"
price = 1.1
final = price * 1.21
# ^ ----X----
# < X--------
# > --------X
print("PRODUCT     PRICE WITHOUT IVA   FINAL")
print("{:^12}{:<15}{:>12}".format(product, price, final))
