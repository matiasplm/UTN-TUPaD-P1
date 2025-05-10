# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.
lista_range = list(range(4,101,4))

#imprimimos las lita
print(lista_range)


# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

#definimos la lista
lista_fruta = ["musica", "mate", "cafe", "correr", "fiestas"]

#Imprimimos el penúltimo elemento
print(lista_fruta[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:
# lista_vacia = []

#definimos la lista
lista_fruta = []

#agregamos los elementos a la lista

lista_fruta.append("manzana")
lista_fruta.append("banana")
lista_fruta.append("pera")

#imprimimos la lista con los cambios
print(lista_fruta)


# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]

#definimos la lista
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

#imprimimos la lista con los cambios
print(animales)


# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

#definimos la lista
numeros = [8, 15, 3, 22, 7]

#con la funcion remove eliminamos un elemento de la lista 
#la funcion max busca el elemento de mayor valor en a lista
numeros.remove(max(numeros))

print(numeros)

#El programa prama realiza es, crea un lista de 5 elementos
#despues con la funcion max busca el elemento de mayor valor
#y con la funcion remove elimina ese valor
#depues imprime la lista con los cambio realizados

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

#definimos la lista
numeros = list(range(10, 31, 5))

#imprimimos los 2 primeros numeros
print(numeros[:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera. autos = ["sedan", "polo", "suran", "gol"]

#definimos la lista
autos = ["sedan", "polo", "suran", "gol"]

#Remplazamos los valores
autos[1:3] = ["fiesta", "focus"]

#imprimimos la lista con los cambios realizados
print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

#definimos la lista
dobles = []

#agragamos el dobles de 5,10 y 15 a la lista
dobles.append(5 * 2)
dobles.append(10 *2)
dobles.append(15 *2)

# Imprimir la lista resultante por pantalla.
print(dobles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
# ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

#definimos la lista
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")

#Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"

#Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

# Imprimir la lista resultante por pantalla.
print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.9], False]

print(lista_anidada)