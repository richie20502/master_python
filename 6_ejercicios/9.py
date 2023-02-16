"""
Hacer un programa que pda numeros 
infinitamente hasta ingresar el numero 111
"""

contador = 1

while contador < 100:
    numero = int(input("numero : "))
    if numero == 111:
        break
    else:
        print(f"Has introduccido el: {numero}")