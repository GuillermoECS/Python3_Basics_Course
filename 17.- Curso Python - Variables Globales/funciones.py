# Guillermo Esteban Castro Sánchez --- Solvo
# 17.- Curso Python - Variables Globales

# Funciones con variables


def funcion_variable(texto):
    # Funcion Palindromo: Se lee igual de adelante para atras
    # Variable local: Los cambios que se dan en la variable, se conservan
    # dentro del contexto del metodo
    texto = texto.replace(' ', '')
    # Valor del texto , variable local
    print(texto)
    return texto == texto[::-1]


# Variable global
texto = ('anita lava la tina')
print(texto)  # Valor del texto antes de funcion_variable
resultado = funcion_variable(texto)
# La variable global no se ve afectada
print(texto)  # Valor del texto despues de funcion_variable
print(resultado)

# Variables locales no pueden ser modificadas y accedidas,
# solo dentro de la funcion.
# Variables globales , podemos modificar y acceder a su valor.


def funcion_variable_global():
    # Funcion Palindromo con variable global
    # Se debe de llamar despues de declarar la variable global
    texto_sin_espacio = texto.replace(' ', '')
    print(texto_sin_espacio)
    return texto_sin_espacio == texto_sin_espacio[::-1]


# Uso de la funcion
print(funcion_variable_global())


def modificar_var_global():  # Funcion para modificar valor global
    global valor_global  # Solo cuando se quiere modificar
    valor_global = "Hola Luna"


def mostrar_valor_global():
    print(valor_global)


# Variable global
valor_global = "Hola Tierra"
mostrar_valor_global()
# Uso de la funcion
modificar_var_global()
mostrar_valor_global()


def crear_variable_global():  # Funcion para crear variable global
    global nueva_variable_global
    nueva_variable_global = "Nueva Variable"


# Uso de funcion
crear_variable_global()
print("Variable global creada en funcion", nueva_variable_global)
