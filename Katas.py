# Ejercicio 1:
# Escribe una función que reciba una cadena de texto como parámetro
# y devuelva un diccionario con las frecuencias de cada letra.
# Los espacios no deben ser considerados.

def frecuencia_letras(texto):
    frecuencias = {}

    # Recorremos cada letra del texto
    for letra in texto:

        # Ignoramos los espacios
        if letra != " ":

            # Si la letra ya existe en el diccionario,
            # aumentamos su contador
            if letra in frecuencias:
                frecuencias[letra] += 1

            # Si no existe, la añadimos con frecuencia 1
            else:
                frecuencias[letra] = 1

    return frecuencias

# Ejercicio 2:
# Dada una lista de números, obtén una nueva lista con el doble
# de cada valor. Usa la función map().

def duplicar(numero):
    return numero * 2


def duplicar_numeros(lista):
    lista_doble = list(map(duplicar, lista))
    return lista_doble

# Ejercicio 3:
# Escribe una función que tome una lista de palabras y una palabra
# objetivo como parámetros. La función debe devolver una lista con
# todas las palabras de la lista original que contengan la palabra objetivo.

def buscar_palabras(lista_palabras, palabra_objetivo):

    resultado = []

    # Recorremos todas las palabras de la lista
    for palabra in lista_palabras:

        # Comprobamos si la palabra objetivo está dentro de la palabra actual
        if palabra_objetivo in palabra:
            resultado.append(palabra)

    return resultado

# Ejercicio 4:
# Genera una función que calcule la diferencia entre los valores
# de dos listas. Usa la función map().

def calcular_diferencia(lista1, lista2):

    # map() irá tomando un elemento de cada lista y restándolos
    diferencias = list(map(lambda x, y: x - y, lista1, lista2))

    return diferencias


# Ejercicio 5:
# Escribe una función que tome una lista de números como parámetro
# y un valor opcional nota_aprobado, que por defecto es 5.
# La función debe devolver una tupla con la media y el estado.

def calcular_nota(lista, nota_aprobado=5):

    media = sum(lista) / len(lista)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return (media, estado)


# Ejercicio 6:
# Escribe una función que calcule el factorial de un número
# de manera recursiva.

def factorial(numero):

    # Caso base: el factorial de 0 y 1 es 1
    if numero == 0 or numero == 1:
        return 1

    # La función se llama a sí misma
    return numero * factorial(numero - 1)


# Ejercicio 7:
# Genera una función que convierta una lista de tuplas
# a una lista de strings. Usa la función map().

def convertir_tuplas(lista_tuplas):

    lista_strings = list(map(str, lista_tuplas))

    return lista_strings


# Ejercicio 8:
# Escribe un programa que pida al usuario dos números
# e intente dividirlos.

try:
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))

    resultado = numero1 / numero2

except ValueError:
    print("Error: debes introducir números válidos.")

except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")

else:
    print("La división ha sido exitosa.")
    print("Resultado:", resultado)


# Ejercicio 9:
# Escribe una función que tome una lista de nombres
# de mascotas y devuelva una nueva lista excluyendo
# ciertas mascotas prohibidas en España.
# Usa la función filter().

def filtrar_mascotas(lista_mascotas):

    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    # Dejamos pasar únicamente las mascotas permitidas
    mascotas_validas = list(
        filter(lambda mascota: mascota not in prohibidas, lista_mascotas)
    )

    return mascotas_validas


# Ejercicio 10:
# Escribe una función que reciba una lista de números
# y calcule su promedio. Si la lista está vacía,
# lanza una excepción personalizada.

class ListaVaciaError(Exception):
    pass


def calcular_promedio(lista):

    if len(lista) == 0:
        raise ListaVaciaError("La lista está vacía.")

    return sum(lista) / len(lista)


try:
    numeros = []

    media = calcular_promedio(numeros)

    print(media)

except ListaVaciaError as error:
    print(error)


# Ejercicio 11:
# Escribe un programa que pida al usuario que introduzca su edad.

try:
    edad = int(input("Introduce tu edad: "))

    if edad < 0 or edad > 120:
        raise ValueError

except ValueError:
    print("Error: introduce una edad válida.")

else:
    print("Tu edad es:", edad)


# Ejercicio 12:
# Genera una función que al recibir una frase
# devuelva una lista con la longitud de cada palabra.
# Usa la función map().

def longitud_palabras(frase):

    palabras = frase.split()

    longitudes = list(map(len, palabras))

    return longitudes


# Ejercicio 13:
# Genera una función que, para un conjunto de caracteres,
# devuelva una lista de tuplas con cada letra en mayúsculas
# y minúsculas. Las letras no pueden estar repetidas.
# Usa la función map().

def convertir_letras(caracteres):

    # set() elimina las letras repetidas
    caracteres_unicos = set(caracteres)

    resultado = list(
        map(
            lambda letra: (letra.upper(), letra.lower()),
            caracteres_unicos
        )
    )

    return resultado

from functools import reduce


# Ejercicio 14:
# Crea una función que retorne las palabras de una lista que comiencen
# con una letra específica. Usa la función filter().

def filtrar_por_letra(lista_palabras, letra):
    palabras_filtradas = list(
        filter(lambda palabra: palabra.startswith(letra), lista_palabras)
    )

    return palabras_filtradas


# Ejercicio 15:
# Crea una función lambda que sume 3 a cada número de una lista dada.

def sumar_tres(lista_numeros):
    resultado = list(map(lambda numero: numero + 3, lista_numeros))

    return resultado


# Ejercicio 16:
# Escribe una función que tome una cadena de texto y un número entero n
# y devuelva las palabras que sean más largas que n. Usa filter().

def palabras_mas_largas(texto, n):
    palabras = texto.split()

    resultado = list(
        filter(lambda palabra: len(palabra) > n, palabras)
    )

    return resultado


# Ejercicio 17:
# Crea una función que tome una lista de dígitos y devuelva
# el número correspondiente. Usa la función reduce().

def convertir_digitos_a_numero(digitos):

    # Multiplicamos el número acumulado por 10 y sumamos
    # el siguiente dígito para colocarlo en la posición correcta.
    numero = reduce(
        lambda acumulado, digito: acumulado * 10 + digito,
        digitos
    )

    return numero


# Ejercicio 18:
# Crea una lista de diccionarios con información de estudiantes
# y extrae los que tengan una calificación mayor o igual a 90.
# Usa la función filter().

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Carlos", "edad": 22, "calificacion": 82},
    {"nombre": "Lucía", "edad": 19, "calificacion": 91}
]

estudiantes_destacados = list(
    filter(
        lambda estudiante: estudiante["calificacion"] >= 90,
        estudiantes
    )
)


# Ejercicio 19:
# Crea una función lambda que filtre los números impares
# de una lista dada.

def filtrar_impares(lista_numeros):
    impares = list(
        filter(lambda numero: numero % 2 != 0, lista_numeros)
    )

    return impares


# Ejercicio 20:
# Para una lista con valores integer y string, obtén una nueva lista
# solamente con los valores int. Usa la función filter().

def filtrar_enteros(lista):
    enteros = list(
        filter(lambda elemento: type(elemento) == int, lista)
    )

    return enteros


# Ejercicio 21:
# Crea una función que calcule el cubo de un número
# mediante una función lambda.

calcular_cubo = lambda numero: numero ** 3


# Ejercicio 22:
# Dada una lista numérica, obtén el producto total
# de todos sus valores. Usa la función reduce().

def calcular_producto(lista_numeros):
    producto = reduce(
        lambda acumulado, numero: acumulado * numero,
        lista_numeros
    )

    return producto


# Ejercicio 23:
# Concatena una lista de palabras. Usa la función reduce().

def concatenar_palabras(lista_palabras):
    texto = reduce(
        lambda acumulado, palabra: acumulado + " " + palabra,
        lista_palabras
    )

    return texto


# Ejercicio 24:
# Calcula la diferencia total de los valores de una lista.
# Usa la función reduce().

def calcular_diferencia_total(lista_numeros):

    # reduce() empieza con los dos primeros valores y continúa
    # restando cada número al resultado acumulado.
    diferencia = reduce(
        lambda acumulado, numero: acumulado - numero,
        lista_numeros
    )

    return diferencia


# Ejercicio 25:
# Crea una función que cuente el número de caracteres
# de una cadena de texto dada.

def contar_caracteres(texto):
    return len(texto)

# Ejercicio 26:
# Crea una función lambda que calcule el resto de la división
# entre dos números dados.

calcular_resto = lambda a, b: a % b


# Ejercicio 27:
# Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(lista_numeros):

    promedio = sum(lista_numeros) / len(lista_numeros)

    return promedio


# Ejercicio 28:
# Crea una función que busque y devuelva el primer
# elemento duplicado en una lista dada.

def buscar_duplicado(lista):

    elementos_vistos = []

    for elemento in lista:

        if elemento in elementos_vistos:
            return elemento

        elementos_vistos.append(elemento)

    return None


# Ejercicio 29:
# Crea una función que convierta una variable en una cadena
# de texto y enmascare todos los caracteres con '#',
# excepto los últimos cuatro.

def enmascarar(texto):

    texto = str(texto)

    longitud = len(texto)

    texto_oculto = "#" * (longitud - 4) + texto[-4:]

    return texto_oculto


# Ejercicio 30:
# Crea una función que determine si dos palabras son anagramas,
# es decir, si están formadas por las mismas letras
# pero en diferente orden.

def son_anagramas(palabra1, palabra2):

    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # sorted() ordena las letras de las palabras para compararlas
    return sorted(palabra1) == sorted(palabra2)


# Ejercicio 31:
# Crea una función que solicite al usuario ingresar una lista
# de nombres y luego solicite un nombre para buscar.

def buscar_nombre():

    nombres = input("Introduce varios nombres separados por comas: ")

    lista_nombres = nombres.split(",")

    nombre_buscado = input("Introduce el nombre que quieres buscar: ")

    if nombre_buscado in lista_nombres:
        print("Nombre encontrado.")

    else:
        raise Exception("El nombre no está en la lista.")


# Ejercicio 32:
# Crea una función que tome un nombre completo y una lista
# de empleados y devuelva el puesto del empleado.

def buscar_empleado(nombre, empleados):

    for empleado in empleados:

        if empleado["nombre"] == nombre:
            return empleado["puesto"]

    return "La persona no trabaja aquí."


# Ejercicio 33:
# Crea una función lambda que sume elementos correspondientes
# de dos listas dadas.

sumar_listas = lambda lista1, lista2: list(
    map(lambda x, y: x + y, lista1, lista2)
)


# Ejercicio 34:
# Crea la clase Arbol.

class Arbol:

    # Inicializamos el árbol con un tronco de longitud 1
    # y una lista vacía de ramas
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    # Aumenta la longitud del tronco en una unidad
    def crecer_tronco(self):
        self.tronco += 1

    # Añade una rama de longitud 1
    def nueva_rama(self):
        self.ramas.append(1)

    # Recorremos todas las ramas y aumentamos su longitud
    def crecer_ramas(self):

        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    # Elimina una rama de una posición concreta
    def quitar_rama(self, posicion):

        if posicion < len(self.ramas):
            self.ramas.pop(posicion)

    # Devuelve la información del árbol
    def info_arbol(self):

        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

    # Ejercicio 36:
    # Crea la clase UsuarioBanco. Representa a un usuario de un banco
    # con su nombre, saldo y si tiene o no cuenta corriente.

    class UsuarioBanco:

        # Inicializamos el usuario con su nombre, saldo
        # y si tiene cuenta corriente
        def __init__(self, nombre, saldo, cuenta_corriente):
            self.nombre = nombre
            self.saldo = saldo
            self.cuenta_corriente = cuenta_corriente

        # Retira dinero del saldo del usuario
        def retirar_dinero(self, cantidad):

            if cantidad > self.saldo:
                raise Exception("No hay suficiente saldo.")

            self.saldo -= cantidad

        # Realiza una transferencia desde otro usuario
        def transferir_dinero(self, otro_usuario, cantidad):

            if cantidad > otro_usuario.saldo:
                raise Exception(
                    f"{otro_usuario.nombre} no tiene suficiente saldo."
                )

            otro_usuario.saldo -= cantidad
            self.saldo += cantidad

        # Añade dinero al saldo
        def agregar_dinero(self, cantidad):
            self.saldo += cantidad

    # Caso de uso

    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    # Añadir 20 unidades a Bob
    bob.agregar_dinero(20)

    # Transferir 80 unidades desde Bob a Alicia
    alicia.transferir_dinero(bob, 80)

    # Retirar 50 unidades de Alicia
    alicia.retirar_dinero(50)

    print(alicia.saldo)
    print(bob.saldo)

    # Ejercicio 37:
    # Crea una función llamada procesar_texto que procese un texto
    # según la opción especificada.

    # Cuenta cuántas veces aparece cada palabra
    def contar_palabras(texto):

        palabras = texto.split()

        resultado = {}

        for palabra in palabras:

            if palabra in resultado:
                resultado[palabra] += 1

            else:
                resultado[palabra] = 1

        return resultado

    # Reemplaza una palabra por otra
    def reemplazar_palabras(texto, palabra_original, palabra_nueva):

        return texto.replace(palabra_original, palabra_nueva)

    # Elimina una palabra del texto
    def eliminar_palabra(texto, palabra):

        palabras = texto.split()

        palabras_filtradas = []

        for p in palabras:

            if p != palabra:
                palabras_filtradas.append(p)

        return " ".join(palabras_filtradas)

    # Función principal que procesa el texto
    def procesar_texto(texto, opcion, *args):

        if opcion == "contar":
            return contar_palabras(texto)

        elif opcion == "reemplazar":
            return reemplazar_palabras(texto, args[0], args[1])

        elif opcion == "eliminar":
            return eliminar_palabra(texto, args[0])

        else:
            return "Opción no válida."

    # Caso de uso

    texto = "hola mundo hola python"

    print(procesar_texto(texto, "contar"))

    print(
        procesar_texto(
            texto,
            "reemplazar",
            "hola",
            "adios"
        )
    )

    print(
        procesar_texto(
            texto,
            "eliminar",
            "hola"
        )
    )

    # Ejercicio 38:
    # Genera un programa que nos diga si es de noche,
    # de día o tarde según la hora proporcionada por el usuario.

    hora = int(input("Introduce la hora (0-23): "))

    if 6 <= hora < 12:
        print("Es de día.")

    elif 12 <= hora < 20:
        print("Es de tarde.")

    elif (20 <= hora <= 23) or (0 <= hora < 6):
        print("Es de noche.")

    else:
        print("Hora no válida.")

    # Ejercicio 39:
    # Escribe un programa que determine qué calificación
    # en texto tiene un alumno en base a su nota numérica.

    nota = int(input("Introduce la nota del alumno: "))

    if 0 <= nota <= 69:
        print("Insuficiente")

    elif 70 <= nota <= 79:
        print("Bien")

    elif 80 <= nota <= 89:
        print("Muy bien")

    elif 90 <= nota <= 100:
        print("Excelente")

    else:
        print("Nota no válida.")

    # Ejercicio 40:
    # Escribe una función que calcule el área de una figura.

    import math

    def calcular_area(figura, datos):

        if figura == "rectangulo":

            base, altura = datos

            return base * altura

        elif figura == "circulo":

            radio = datos[0]

            return math.pi * radio ** 2

        elif figura == "triangulo":

            base, altura = datos

            return (base * altura) / 2

        else:

            return "Figura no válida."

    # Ejercicio 41:
    # Programa que calcula el precio final de una compra
    # aplicando un cupón de descuento.

    precio = float(input("Introduce el precio del artículo: "))

    cupon = input("¿Tienes un cupón de descuento? (sí/no): ")

    if cupon.lower() == "sí" or cupon.lower() == "si":

        descuento = float(
            input("Introduce el valor del descuento: ")
        )

        if descuento > 0:

            precio_final = precio - descuento

            print(
                "El precio final es:",
                precio_final,
                "euros"
            )

        else:

            print("El descuento no es válido.")

    else:

        print(
            "El precio final es:",
            precio,
            "euros"
        )