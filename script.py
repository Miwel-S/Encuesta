#Autor: Miguel Silva
#Esto es una prueba

#1 prueba
texto="lorem"
print(texto)

#2 Tabla de multiplicar de un numero ingresado por el usuario
num=int(input("Ingrese el numero: "))
for i in range(11):
	print(f"{num} x {i} = {num*i}\n")

#3 Funcion factorial con un numero ingresado por el usuario
def factorial(x):
	num=1
	for i in range(1, x+1):
		num*=i
	return num
a=int(input("Ingrese un numero: "))
print(f"El factorial de {a} es {factorial(a)}")