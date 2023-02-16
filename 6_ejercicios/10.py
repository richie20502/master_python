"""
el programa tiene que pedir la nota de 15 alumnos
y sacar por pantalla cuantos han aprobado y cuantos han suspendido
"""

contador = 0
aprobados = 0
suspendidos = 0
numero_alumnos  = int(input("Cuantos añumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f"que nota quieres ponerle al alumno {contador}"))

    if nota >= 5:
        aprobados += 1
    else:
        suspendidos +=1

    contador += 1