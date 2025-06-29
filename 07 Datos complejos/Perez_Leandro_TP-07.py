# Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

precios_frutas["Naranaja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas["Naranaja"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Pera"] = 2800

print(precios_frutas)


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
frutas_solas = precios_frutas.keys()

print(frutas_solas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos ={"Matias": 1166446867, "Tamara":11588676,"Alejandro":115886990,"Zoe":113545000,"Gonzalo":114569888 }
nombre = input("Ingrese el nombre del contacto: ")

if nombre in contactos:
    print(f"El numero del contacto {nombre} es: {contactos[nombre]}")
else:
    print(f"El numero del contacto {nombre} no existe")
    
# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra
#Definimos funcion
def frecuenia_palabras(palabras_frase):
    frecuencia = {}
    for i in palabras_frase:
        if i in frecuencia:
            frecuencia[i] += 1
        else:
            frecuencia[i] = 1
    return frecuencia

#Solicitud de al Usuario
frase = input("Ingrese una frase: ")

#convertimos las frases en palabras
palabras_frase = frase.split()
#palabras a set
palabras_unicas = set(palabras_frase)

#Imprimimos los resultados
print(f"Palabras unicas: {palabras_unicas}")
print(f"Diccionario: {frecuenia_palabras(palabras_frase)}")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

#Definicion de funcion
def diccionario_nota_alumnos():
    #creamos un diccionario vacio
    alumnos = {}
    #un ciclo for para recorrer los 3 alumnos
    for i in range(3):
        nombre_alumno = input(f"Ingrese el Nombre del Alumno {i+1}: ")
        notas_alumnos=[]
        for j in range (3):
            nota = float(input(f"Ingrese la nota {j+1}: "))
            notas_alumnos.append(nota)
        alumnos[nombre_alumno]= tuple(notas_alumnos)
    return alumnos

alumnos = diccionario_nota_alumnos()
print(f"El promedio de los alumnos es: ")
for nombre,notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

#Set de notas
parcial1 = {103,105,160,104}
parcial2 = {104,105,120,156}

#Imprimomos los resultados
# Estudiantes que aprobaron ambos parciales (intersección)
print("Estudiantes que aprobaron ambos parciales: ", parcial1 & parcial2)
# Estudiantes que aprobaron solo uno de los dos parciales (diferencia simétrica)
print("Estudiantes que aprobaron solo uno de los dos: ", parcial1 ^ parcial2)
# Estudiantes que aprobaron al menos un parcial (unión)
print("Estudiantes que aprobaron al menos un parcial: ", parcial1 | parcial2)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.



# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

#Diccionario de la agenda
agenda = {
    ("lunes", "07:30"): "GYM",
    ("lunes", "10:30"): "Reunion",
    ("martes","14:00"):"Dentista"
}
#solicitud al usuario
dia = input("Ingrese el dia: ")
horario =input("Ingrese el Horio (Formato 10:00): ")

clave=(dia, horario)

if clave  in agenda:
    print(f"El dia {dia}  {horario} horas esta agendado: {agenda[clave]}")
else:
    print(f"El dia {dia}  {horario} horas no existen actividades agendades")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

orinal = {
    "Argentina":"Buenos Aires", 
    "Chile":"Santiago",
    "Bolivia": "La Paz"
}

invertido={}

for paises,capitales in orinal.items():
    invertido[capitales]=paises

print(f"Diccionario Orinal {orinal}")
print(f"Diccionario invertido {invertido}")
