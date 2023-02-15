#creacion de variables
variable_t = "texto 1"
variable_t_2 = "otro texto"
numero = 20
decimal = 1.2

#imprimir varibles
print(variable_t)
print(variable_t_2)
print(numero)
print(decimal)

#modificacion de varibles (asignacion de nuevos valores)
numero = 10
decimal =3.4

#imprimir de variables modificadas
print(numero)
print(decimal)

#concatenación de variables
variable_concatenar = variable_t + " " + variable_t_2

print(variable_concatenar)
print(f"{variable_t} {variable_t_2}")
print("texto 1 {} texto 2 {} :".format(variable_t,variable_t_2))