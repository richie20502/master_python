#ciclo for

contador = 0
resultado = 0
for contador in range(0,5):
    print("voy por el "+ str(contador))
    resultado = resultado + contador
print(f"el resultado es: {resultado}")