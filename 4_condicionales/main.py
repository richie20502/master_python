#primer ejecrcio condicional if
numero = 10

if numero == 10:
    print(f"El valor de la variable es {numero}")
else:
    print("no es igual a 10")

#operadores de comparacion
"""
== igual 
!= diferente
< menor que 
> mayor que
<= menor igual que 
>= mayor igual que
"""
year = int(input("dime el año en el que estamos ?"))

if year >= 2023:
    print("estamos en 2023 en ")
else 
    print("no estas al año")

#ifs anidados

mayor = 18
edad = 20
if  edad >=mayor:
    print("eres mayor de edad")
    if edad == mayor:
        print("tienes exactamente 18")
    else:
        print(f"tienes {edad}")
else:
    print("no eres mayor de edad")