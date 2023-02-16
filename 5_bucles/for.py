#ciclo for

contador = 0
resultado = 0
for contador in range(0,5):
    print("voy por el "+ str(contador))
    resultado = resultado + contador
print(f"el resultado es: {resultado}")

#ejemplo tabla de multiplicar

tabla = 2

for tabla_m in range (0, 10):
    print(f"{tabla} x {tabla_m} = {tabla*tabla_m}")