# Guillermo Esteban Castro Sánchez --- Solvo
# 16.- Curso Python - Funciones parte 2


def suma(valor1, valor2):  # Funcion de suma
    return valor1+valor2


print(suma(34, 45))  # Forma de parametros #1


def division(valor1, valor2):  # Funcion de Division
    return valor1//valor2

# Uso de funcion


print(division(30, 2))  # Forma de parametros #1

print(division(valor2=60, valor1=120))  # Forma de parametros #2


def multiplicacion(valor1, valor2=9):
    # Multiplicacion con parametro default valor2
    return valor1*valor2


resultado = multiplicacion(3)
print(resultado)


# Las funciones pueden devolver diferentes tipos de valores


def multiples_valores():
    # Funcion que devuelve multiples valores de diferentes tipos
    return "string", 1, 'hola', 8.9, True


# Uso de funcion
#  El interprete le asigna el valor a cada variable
string1, entero, string2, flotante, booleano = multiples_valores()
print(string1, ",", entero, ",", string2, ",", flotante, ",", booleano)

# Asignar funciones a variables
variable_funcion = multiplicacion
print(variable_funcion(9))


def mostrar_resultado(funcion):
    # Llamar funciones dentro de funciones
    print(funcion(3, 4))


# Uso de la funcion que llama una funcion dentro de otra funcion
# print es una funcion
mostrar_resultado(multiplicacion)
