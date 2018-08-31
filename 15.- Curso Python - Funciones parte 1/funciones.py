# Guillermo Esteban Castro Sánchez --- Solvo
# 15.- Curso Python - Funciones parte 1

# Estructura de una funcion
# def nombre_de_la_funcion:
#     codigo
# Funcion Vacia


def funcion_vacia():
    pass


def factorial_numero5():
    numero = 5
    factorial = 1
    while(numero > 0):
        factorial *= numero
        numero -= 1
    print(factorial)  # No regresa ningun valor, solo muestra en terminal


# Invocar funcion
factorial_numero5()

# Argumentos: Entradas a funciones que van permitir realizar ciertas acciones


def factorial_numero(numero):  # Factorial de cualquier numero
    factorial = 1
    while(numero > 0):
        factorial *= numero
        numero -= 1
    print(factorial)  # No regresa ningun valor, solo muestra en terminal


# Invocar funcion
factorial_numero(6)


def factorial_numero(numero):  # Factorial de cualquier numero,retornando valor
    factorial = 1
    while(numero > 0):
        factorial *= numero
        numero -= 1
    return factorial  # No regresa ningun valor, solo muestra en terminal


# Invocar funcion
print(factorial_numero(9))  # Mostrar valor retornado mediante print()
