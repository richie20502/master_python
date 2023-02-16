#listas
numero = 10
numeros =[2,7,8,34,10]
nombre = list(("n1", "n2", "n3", "n5"))
years = list(range(2010,2020))

print(numero)
print(numeros)
print(nombre)

#indices
print(numeros[0])
print(nombre[3])

#agregar elemento a lista

numeros.append("89")
print(numeros)

#recorrer lista
for numero in numeros:
    print(f"{numeros.index(numero) + 1} . {numero}")