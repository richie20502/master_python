#variables locales globales


#Globales
frase = "frace global"

def holaM():
    frase = "Hola Mundo !!"
    print(frase)
    year = 2023
    print(year)

    global website
    website = "misitio.com"
    print("dentro: ", website)
    return "datos retornados" + str(year)

print(holaM())
print("fuera ", website)