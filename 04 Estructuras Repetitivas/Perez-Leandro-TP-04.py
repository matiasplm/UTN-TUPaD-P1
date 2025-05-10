#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#bucle for hata 100
for i in range (101):
    print(i)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

#Inicializamos el contador de digito
contadorDigitos = 0

#Solicitud al usuario
numero = int (input(" Ingrese un numero entero "))
aux = numero

#bucle para contar digitos
while aux > 0 :
    contadorDigitos = contadorDigitos + 1
    aux = aux // 10

#imprimimos la cantidad de digitos
print (f"La cantidad de digitos del numero {numero} es: {contadorDigitos}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

#Incializamos variables
suma = 0

#Solicitud al usuario
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

#Si num1 es mayor a num2 intercabiamos los valores 
if num1 > num2 :
    num1 , num2 =  num2 , num1

#Buce for para sumar los numeros comprendidos entre num1 y num2
for i in range (num1 +1 ,num2):
    suma = suma + i

#mostramos los resultados 
print(f"La suma  de los numeros comprendidos entre {num1} y {num2} es: {suma}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

#bucle for 
for i in range(100,-1,-2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# Inicializamos variables
suma = 0

#Solicitud al usuario
fin = int(input("Ingrese un numero enero positivo: "))

#bucle for
for i in range (fin + 1):
    suma = suma + i

#mostramos el resultado de la suma
print(f"La suma de los numeros comprendido entre 0 y {fin} es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#Inicializamos Variables
pares = 0
impares = 0
negativos = 0
positivos = 0


for i in range(100):
    #Solicitud al usuario
    numero = int(input( "Ingrese un numero entero: "))
    
    #contamos los numeros positivos  y negativos
    if numero > 0:
        positivos += 1
    else:
        negativos += 1
    
    #contamos los numeros pares e impares 
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

#mostramos lo resultados
print(f"La cantidad de numeros positivos ingresados es: {positivos}")
print(f"La catindad de numero negativos ingresados es: {negativos}")
print(f"La cantidad de numeros pares ingresados es: {pares}")
print(f"La catindad de numero impares ingresados es: {impares}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# Inicializamos Variables
suma = 0
fin = 100

#bucle for
for i in range(fin):
    #Solicitud al usuario
    numero = int(input( "Ingrese un numero entero: "))
    
    #sumamos los numeros ingresados
    suma += numero

#calcuculamos la media
media = suma / fin

#mostramos lo resultados
print(f"La Media de los {fin} numeros ingreasdos es : {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#Inicializamos Variables
numeroInvertido = 0

#Solicitud al usuario
numero = int(input( "Ingrese un numero entero: "))

aux = numero

#bucle while para invertir los digitos del numero
while aux > 0:
    #sacamos el digito
    digito = aux % 10 
    #sumamos el digito extraido
    numeroInvertido = numeroInvertido * 10 + digito
    #disminuimos el numero
    aux = aux // 10 

#mostramos el resultado
print(f"El numero ingresado es: {numero}")
print(f"El numero invirtiendo sus digito es: {numeroInvertido}")
