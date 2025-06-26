# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

#Definición de Funciones
def recur_factorial_numero(numero):
    if numero == 0:
        return 1
    else: 
        return numero * recur_factorial_numero(numero-1)

# #Programa Principal
numero = int(input("Ingrese un Numero entero, para calcular la factorial: "))
print(f"La factorial del numero {numero}! es: {recur_factorial_numero(numero)}")


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.


#Definición de Funciones
def recur_fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return recur_fibonacci(posicion-1) + recur_fibonacci(posicion-2)
    
# #Programa Principal
posicion = int(input("Ingrese un Numero entero,para calcular la serie de Fibonacci hasta esa posicion: "))
print(f"La serie Fibonacci hasta el numero{posicion} es: {recur_fibonacci(posicion)}")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.

#Definición de Funciones
def recur_potencia(numero, exponete):
    if exponete == 0:
        return 1
    else:
        return numero * recur_potencia(numero,exponete-1)

#Programa Principal
numero = 3
exponete = 3
print(f"La potecia del numero {numero} elevo al exponete {exponete} es: {recur_potencia(numero,exponete)}")


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.


#Definición de Funciones
def recur_decimal_a_binario(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return recur_decimal_a_binario(numero // 2) + str(numero % 2)

#Programa Principal
numero = int(input("Ingrese el Numero decimal que sea convertir a binario: "))
print(f"El numero {numero} es binario es: {recur_decimal_a_binario(numero)}")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

#Definición de Funciones
def es_palindromo(palabra):
    if len(palabra) >= 1:
        return True    
    
    if palabra[0] != palabra[-1]:
        return False

    es_palindromo(palabra[1:-1])

#Programa Principal
palabra = input("cadena de texto sin espacios ni tildes: ")
print(f"La cadena {palabra} es palidromo : {es_palindromo(palabra)}")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

#Definición de Funciones
def suma_digitos(n):
    if n==0:
        return 0
    else:
        return suma_digitos(n//10) + n % 10

#Programa Principal
n=305

print(f"La suma de los digitos del numero {n} es: {suma_digitos(n)}")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.

#Definición de Funciones
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return contar_bloques(n-1) + n
        
#Programa Principal

n_bloques = int(input("Ingrese el número de bloques en el nivel más bajo: "))
print(f"Los bloques que necesita para construir toda la pirámide son {contar_bloques(n_bloques)}")

# 8)Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 

#Definición de Funciones
def contar_digito(numero, digito):
    if numero <= 0:
        return 0
    else:
        if numero % 10 == digito:
            return contar_digito(numero//10, digito) + 1
        else:
            return contar_digito(numero//10, digito)

#Programa Principal

numero = int(input("Ingrese el Numero entero positivo: "))
digito = int(input("Ingrese el digito: "))

print(f"En el numero {numero} el digito {digito} se reoite: {contar_digito(numero, digito)}")