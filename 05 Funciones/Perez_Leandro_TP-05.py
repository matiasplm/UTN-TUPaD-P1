# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def saludo():
    print("Hola mundo!")

saludo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

#Definicion de Funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}")

#Programa Principal
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.

#Definicion de Funciones
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Programa Principal
nombre = input("Ingrese su Nombre: ")
apellido = input("Ingrese su Apellido: ")
edad = input("Ingrese su Edad: ")
residencia = input("Ingrese su Residencia: ")
informacion_personal(nombre,apellido,edad,residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

# Definicion de Funciones
def calcular_area_circulo(radio):
    area  = math.pi * radio**2
    return area

def calcular_perimetro_circulo(radio):
    perimetro  =  2 * math.pi * radio
    return perimetro

#Programa Principal
import math
radio = float(input("Ingrese el Area del Circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El Circulo de Radio {radio}, el area es {area} y el perimetro es {perimetro}")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

# Definicion de Funciones
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

#Programa Principal
segundos = float(input("Ingrese los segundos: "))
horas = segundos_a_horas(segundos)
print(f"Los {segundos} segundos, equivalen a {horas} horas")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Definicion de Funciones
def tabla_multiplicar(numero):
    for i in range (1, 11):
        print (f"{numero} * {i} = {numero*i}")
        
#Programa Principal
numero = int(input("Ingrese un numero :"))
tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

#Definicion de Funciones
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    tupla_operaciones = (suma, resta, multiplicacion, division)
    return tupla_operaciones

#Programa Principal
numero1 = float(input("Ingrese el primer numero :"))
numero2 = float(input("Ingrese el segundo numero :"))
operaciones=operaciones_basicas(numero1, numero2)

print(f"El primer numero es: {numero1}")
print(f"El segundo numero es: {numero2}")
print(f"{numero1} + {numero2} = {operaciones[0]}")
print(f"{numero1} - {numero2} = {operaciones[1]}")
print(f"{numero1} * {numero2} = {operaciones[2]}")
print(f"{numero1} / {numero2} = {operaciones[3]}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

# Definicion de Funciones
def calcular_imc(peso, altura):
    imc = round(peso / altura**2, 2)
    return imc

#Programa Principal
peso = float(input("Ingrese Peso(en kilos): "))
altura = float(input("Ingrese Altura(en metros): "))
imc = calcular_imc(peso, altura)

print(f"Peso {peso}kg altura {altura}m el IMC es: {imc}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# Definicion de Funciones
def celsius_a_fahrenheit(celsius):
    return 9 / 5 * celsius + 32

#Programa Principal
gradosCelsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(gradosCelsius)

print(f"{gradosCelsius} grados Celsius equivalen a: {fahrenheit} grados Fahrenheit")


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

#Definicion de Funciones
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Programa Principal
num1 = float(input("Ingrese el Primer Numero : "))
num2 = float(input("Ingrese el Segundo Numero : "))
num3 = float(input("Ingrese el Tercer Numero : "))
promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio de los numeros ingrasado es : {promedio}")