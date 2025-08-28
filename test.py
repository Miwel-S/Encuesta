#Autor: Miguel Silva
#Primera version

#1 Estructuras de control
#if, for, while, switch, dowhile

#Prueba
#Estruturar un programa que mencione cuando la calificacion del usuario es meritoria (4.5 a 5 es meritorio)

def xd():
    calificacion = float(input("Escriba su calificacion numerica entre 0 y 5: "))
    if calificacion>=4.5:
        print("Su nota es meritoria.")
    else:
        print("Su nota no es meritoria.")

#Ejercicio 21: Escribir un programa que lea dos números del teclado y diga cual es el
#mayor y cual el menor.

def xd2():
    num1= float(input("Escriba el primer numero: "))
    num2= float(input("Escriba el  segundo numero: "))

    if num1>num2:
        print(f"{num1} es el numero mayor y {num2} es el numero menor.")
    else:
        print(f"{num2} es el numero mayor y {num1}es el numero menor.")

#Ejercicio 22: Escribir un programa que lea un número entero por el teclado e imprima
#todos los número impares menores que él.

def xd3():
    num=int(input("Escriba un numero entero: "))
    for i in range(num, 0, -1):
        if i%2 != 0:
            print(i)
