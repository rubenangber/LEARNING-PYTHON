listaA = [1 == 1, 2 == 2, 3 == 4]
res = any(listaA) #Devuelve True si alguna condicion se cumple
print(res)

listaB = [1 == 1, 2 == 2, 3 == 4]
res = all(listaB) #Devuelve True si TODAS las condiciones se cumplen
print(res)