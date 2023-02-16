"""
Escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismos) de los 60 primeros 
numeros naturales. resolverlo con for o while
"""

contador = 0
while contador <= 60:
    cuadrado = contador*contador
    print(f"el cuadrado de {contador} = {cuadrado}")
    contador +=1