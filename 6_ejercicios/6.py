"""
Mostrar todas las tablas de multiplicar del 1 al 10
y despues multiplicar del 1 al 10
"""

for cabecera in range(1, 11):
    print(f"tabla del {cabecera}")

    for numero in range(1,11):
        print(f"{numero} x {cabecera} = {numero*cabecera}")