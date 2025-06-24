# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

#Definición de Funciones
def recur_factorial_numero(numero):
    if numero == 0:
        return 1
    else: 
        return numero * recur_factorial_numero(numero-1)

#Programa Principal
numero = int(input("Ingrese un Numero entero, para calcular la factorial: "))
print(f"La factorial del numero {numero}! es: {recur_factorial_numero(numero)}")


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.


#Definición de Funciones
def recur_fibonacci(numero):
    

#Programa Principal
numero = int(input("Ingrese un Numero entero,para calcular la serie de Fibonacci hasta esa posicion: "))
print(f"La serie Fibonacci hasta el numero{numero} es: {recur_fibonacci(numero)}")






# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.







# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
