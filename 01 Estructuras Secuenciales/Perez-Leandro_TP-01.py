#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print (' “Hola Mundo!” ')

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingrese su nombre ")

print (f'"Hola {nombre}!"')

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla.

nombre = input ("Ingrese su Nombre: ")
apellido = input ("Ingrese su Apellido: ")
edad = input ("Ingrse su Edad: ")
lugar= input ("Ingrese su lugar de residencia: ")

print (f"Soy {nombre}, tengo {edad} años y vivo en {lugar}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float (input ("Ingrese el radio del circulo: "))

import math
area = math.pi * radio**2

print (f"El area del circulo es :{area}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale

segundos = int (input ("Ingrese la cantidad de segundos :"))

horas = segundos / 3600

print (f"{segundos} segundos equivale a {horas} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un Numero :"))

print (f"{numero} x 1 = {numero * 1}")
print (f"{numero} x 2 = {numero * 2}")
print (f"{numero} x 3 = {numero * 3}")
print (f"{numero} x 4 = {numero * 4}")
print (f"{numero} x 5 = {numero * 5}")
print (f"{numero} x 6 = {numero * 6}")
print (f"{numero} x 7 = {numero * 7}")
print (f"{numero} x 8 = {numero * 8}")
print (f"{numero} x 9 = {numero * 9}")
print (f"{numero} x 1 = {numero * 10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("Ingrese dos números enteros distintos del 0")
num1 = int(input("Ingrese el Primer Numero :"))
num2 = int(input("Ingrese el Primer Numero :"))

print (f"{num1} + {num2} = {num1 + num2}")
print (f"{num1} / {num2} = {num1 / num2}")
print (f"{num1} x {num2} = {num1 * num2}")
print (f"{num1} - {num2} = {num1 - num2}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:

altura = float(input("Ingrse su altura en Mentros :"))
peso = float(input("Ingrese su peso en Kilogramos :"))

imc = peso / (altura**2)

print(f"Su índice de masa corporal es : {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 

gradosCelsius = float(input("Ingrese una temperatura en grados Celsius"))

gradosFahrenheit = 9 / 5 * gradosCelsius + 32

print(f"{gradosCelsius} grados Celsius equivalen a :{gradosFahrenheit} grados Fahrenheit")

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.

num1 = float(input("Ingrese el Primer Numero : "))
num2 = float(input("Ingrese el Segundo Numero : "))
num3 = float(input("Ingrese el Tercer Numero : "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los numeros ingrasado es : {promedio}")