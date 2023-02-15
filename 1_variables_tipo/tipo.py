#tipo de dato none
none = None
string = "hola mundo"
integer = 10
double = 1.90
boolean = True
list = [1,2,3,4,5,6]
listS = [1,"hola",10]
tupla = ("esta","es","una","tupla")
json = { "a" : "esta es A", "b": "estas es B"}
rango = range(10)
dato_byte = b"byte"

print(none)

#tipo de dato 
print(type(none))
print(type(string))
print(type(integer))
print(type(double))
print(type(boolean))
print(type(list))
print(type(listS))
print(type(tupla))
print(type(json))
print(type(rango))
print(type(dato_byte))

#convertir tipo de datos
texto = "Hola soy un texto"
numerico = str(102)
print(texto + " " + numerico)

num1 = int(numerico)
num2 = float(numerico)
print(type(num1))
print(type(num2))