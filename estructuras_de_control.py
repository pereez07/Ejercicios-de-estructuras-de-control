# ==========================================
# 1. BIFURCACIONES
# ==========================================

'''
Algoritmo: Signo de un número
Entrada: Un número
salida: "positivo", "negativo" o "cero"
bloque de desarrollo:
1. Si el número es mayor que 0, devolver "positivo".
2. Si el número es menor que 0, devolver "negativo".
3. En cualquier otro caso, devolver "cero".
'''
# Algoritmo Signo de un número en python
def signo_numero(numero):
    if numero > 0:
        return 'positivo'
    elif numero < 0:
        return 'negativo'
    else:
        return 'cero'

'''
Algoritmo: Año bisiesto
Entrada: Un año (entero)
salida: True si es bisiesto, False si no lo es
bloque de desarrollo:
1. Si el año es divisible por 4 Y NO es divisible por 100, es bisiesto (True).
2. Si el año es divisible por 400, también es bisiesto (True).
3. En cualquier otro caso, no es bisiesto (False).
'''
# Algoritmo Año bisiesto en python
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False

'''
Algoritmo: El mayor de tres números
Entrada: Tres números (a, b, c)
salida: El número mayor
bloque de desarrollo:
1. Si 'a' es mayor o igual que 'b' y 'c', devolver 'a'.
2. Si 'b' es mayor o igual que 'a' y 'c', devolver 'b'.
3. Si no se cumple lo anterior, devolver 'c'.
'''
# Algoritmo El mayor de tres números en python
def mayor_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

'''
Algoritmo: Categoría de envío según el peso
Entrada: Peso en kilos
salida: Categoría del paquete ("Sobre", "Paquete pequeño", "Paquete grande", "Voluminoso")
bloque de desarrollo:
1. Si el peso es <= 1, devolver "Sobre".
2. Si el peso es > 1 y <= 5, devolver "Paquete pequeño".
3. Si el peso es > 5 y <= 20, devolver "Paquete grande".
4. Si el peso es > 20, devolver "Voluminoso".
'''
# Algoritmo Categoría de envío según el peso en python
def categoria_envio(peso_kg):
    if peso_kg <= 1:
        return 'Sobre'
    elif peso_kg <= 5:
        return 'Paquete pequeño'
    elif peso_kg <= 20:
        return 'Paquete grande'
    else:
        return 'Voluminoso'


# ==========================================
# 2. ITERACIONES
# ==========================================

'''
Algoritmo: Suma de pares entre 1 y n
Entrada: Un número n
salida: Suma de los números pares
bloque de desarrollo:
1. Inicializar una variable 'suma' a 0.
2. Para cada número desde 1 hasta n:
    3. Si el número es par (divisible por 2), sumarlo a 'suma'.
4. Devolver 'suma'.
'''
# Algoritmo Suma de pares entre 1 y n en python
def suma_pares(n):
    suma = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            suma += i
    return suma

'''
Algoritmo: Factorial con bucle
Entrada: Un número n
salida: Factorial de n
bloque de desarrollo:
1. Inicializar variable 'resultado' a 1.
2. Para cada número desde 1 hasta n:
    3. Multiplicar 'resultado' por ese número.
4. Devolver 'resultado'.
'''
# Algoritmo Factorial con bucle en python
def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

'''
Algoritmo: Contar vocales de una palabra
Entrada: Una palabra (texto)
salida: Número de vocales
bloque de desarrollo:
1. Inicializar 'contador' a 0.
2. Convertir la palabra a minúsculas.
3. Para cada letra en la palabra:
    4. Si la letra es a, e, i, o, u, incrementar 'contador' en 1.
5. Devolver 'contador'.
'''
# Algoritmo Contar vocales de una palabra en python
def contar_vocales(palabra):
    contador = 0
    for letra in palabra.lower():
        if letra in 'aeiou':
            contador += 1
    return contador

'''
Algoritmo: Tabla de multiplicar
Entrada: Un número
salida: Impresión de la tabla de multiplicar del 1 al 10
bloque de desarrollo:
1. Para cada número 'i' del 1 al 10:
    2. Calcular número * i.
    3. Imprimir el texto con el formato "numero x i = resultado".
'''
# Algoritmo Tabla de multiplicar en python
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero}x{i}={numero*i}")


# ==========================================
# 3. FUNCIONES
# ==========================================

'''
Algoritmo: Promedio de una lista de números
Entrada: Una lista de números
salida: La media aritmética
bloque de desarrollo:
1. Calcular la suma total de los números de la lista.
2. Contar cuántos números hay en la lista.
3. Dividir la suma entre la cantidad de números y devolver el resultado.
'''
# Algoritmo Promedio de una lista de números en python
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

'''
Algoritmo: Texto en mayúsculas y número de palabras
Entrada: Una frase (texto)
salida: La frase en mayúsculas y el recuento de palabras
bloque de desarrollo:
1. Convertir la frase a mayúsculas.
2. Separar la frase en palabras y contar cuántas hay.
3. Devolver ambos resultados.
'''
# Algoritmo Texto en mayúsculas y número de palabras en python
def analizar_frase(frase):
    frase_mayusculas = frase.upper()
    numero_palabras = len(frase.split())
    return frase_mayusculas, numero_palabras

'''
Algoritmo: Validar contraseña
Entrada: Una contraseña y una longitud mínima (por defecto 8)
salida: True si cumple la longitud, False si no
bloque de desarrollo:
1. Calcular la longitud de la contraseña.
2. Si la longitud es mayor o igual a longitud_minima, devolver True.
3. Si no, devolver False.
'''
# Algoritmo Validar contraseña en python
def validar_contrasena(contrasena, longitud_minima=8):
    return len(contrasena) >= longitud_minima

'''
Algoritmo: Conversión de temperatura (Celsius a Fahrenheit)
Entrada: Grados Celsius
salida: Grados Fahrenheit
bloque de desarrollo:
1. Multiplicar Celsius por 9/5.
2. Sumar 32 al resultado y devolverlo.
'''
# Algoritmo Conversión de temperatura (C a F) en python
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

'''
Algoritmo: Conversión de temperatura (Fahrenheit a Celsius)
Entrada: Grados Fahrenheit
salida: Grados Celsius
bloque de desarrollo:
1. Restar 32 a Fahrenheit.
2. Multiplicar el resultado por 5/9 y devolverlo.
'''
# Algoritmo Conversión de temperatura (F a C) en python
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


# ==========================================
# 4. FUNCIONES RECURSIVAS
# ==========================================

'''
Algoritmo: Factorial recursivo
Entrada: Un número n
salida: Factorial de n
bloque de desarrollo:
1. Caso base: si n es 0, devolver 1.
2. Caso recursivo: devolver n multiplicado por la función factorial de n-1.
'''
# Algoritmo Factorial recursivo en python
def factorial_recursivo(n):
    if n == 0:
        return 1
    return n * factorial_recursivo(n - 1)

'''
Algoritmo: Sucesión de Fibonacci
Entrada: Término n
salida: Valor en la sucesión de Fibonacci
bloque de desarrollo:
1. Caso base: si n es 0, devolver 0. Si n es 1, devolver 1 (es decir, si n <= 1, devolver n).
2. Caso recursivo: devolver la suma de fibonacci(n-1) y fibonacci(n-2).
'''
# Algoritmo Sucesión de Fibonacci en python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

'''
Algoritmo: Suma recursiva de una lista
Entrada: Una lista de números
salida: Suma de los elementos
bloque de desarrollo:
1. Caso base: si la lista está vacía, devolver 0.
2. Caso recursivo: devolver el primer elemento más la suma recursiva del resto de la lista.
'''
# Algoritmo Suma recursiva de una lista en python
def suma_lista(numeros):
    if not numeros:
        return 0
    return numeros[0] + suma_lista(numeros[1:])

'''
Algoritmo: Invertir una cadena de texto
Entrada: Cadena de texto
salida: Cadena de texto invertida
bloque de desarrollo:
1. Caso base: si el texto está vacío, devolver un texto vacío.
2. Caso recursivo: devolver el texto invertido excluyendo la primera letra, y concatenar la primera letra al final.
'''
# Algoritmo Invertir una cadena de texto en python
def invertir_texto(texto):
    if not texto:
        return ""
    return invertir_texto(texto[1:]) + texto[0]


# ==========================================
# 5. EXCEPCIONES
# ==========================================

'''
Algoritmo: División segura
Entrada: Dos números (a, b)
salida: Resultado de la división o mensaje de error
bloque de desarrollo:
1. Intentar dividir 'a' entre 'b' y devolver el resultado.
2. Si se produce un error por división entre cero, capturarlo y devolver el mensaje "Error: división entre cero".
'''
# Algoritmo División segura en python
def division_segura(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división entre cero"

'''
Algoritmo: Convertir texto a número
Entrada: Texto
salida: Número entero o mensaje de error
bloque de desarrollo:
1. Intentar convertir el texto a número entero y devolverlo.
2. Si se produce un error de formato, capturarlo y devolver "Error: no es un número".
'''
# Algoritmo Convertir texto a número en python
def convertir_a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        return "Error: no es un número"

'''
Algoritmo: Acceso seguro a una lista
Entrada: Una lista y una posición
salida: El elemento en esa posición o mensaje de error
bloque de desarrollo:
1. Intentar acceder al elemento de la lista en la posición indicada y devolverlo.
2. Si la posición no existe, capturar el error y devolver "Error: posición fuera de rango".
'''
# Algoritmo Acceso seguro a una lista en python
def obtener_elemento(lista, posicion):
    try:
        return lista[posicion]
    except IndexError:
        return "Error: posición fuera de rango"

'''
Algoritmo: Calculadora con control de errores
Entrada: Dos textos (texto_a, texto_b) y una operacion
salida: Resultado o mensaje de error
bloque de desarrollo:
1. Intentar convertir ambos textos a números decimales (float).
2. Si la operación es "suma", devolver la suma de ambos.
3. Si la operación es "division", devolver la división del primero entre el segundo.
4. Si ocurre un error de valor (texto no numérico), devolver "Error: valor no numérico".
5. Si ocurre un error de división entre cero, devolver "Error: división entre cero".
'''
# Algoritmo Calculadora con control de errores en python
def calculadora_segura(texto_a, texto_b, operacion):
    try:
        a = float(texto_a)
        b = float(texto_b)
        if operacion == 'suma':
            return a + b
        elif operacion == 'division':
            return a / b
    except ValueError:
        return "Error: valor no numérico"
    except ZeroDivisionError:
        return "Error: división entre cero"