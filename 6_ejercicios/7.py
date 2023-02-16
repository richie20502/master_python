"""
Hacer un ejercicio que muestre todos los numeros impares
entre dos numeros que decida el usuario
"""

n1 =  1
n2 = 200

for x in range(n1, (n2 + 1)):
    if x%2 ==0:
        print(f"{x} es PAR")
    else:
        print(f"{x} es IMPAR")