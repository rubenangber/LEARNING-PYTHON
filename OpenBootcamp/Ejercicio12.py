paises = input("Introduce paises separados por ',' >> ")

paises = paises.split(',')
paises = list(set(paises))
paises.sort()

print(", ".join(paises))