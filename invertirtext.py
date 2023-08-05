texto = input("Introduce el texto >> ")
lenth = len(texto)
final = ''

for i in range(lenth):
    final = final + texto[lenth - 1 - i]

print(f'El texto invertido es >> {final}')