# Guillermo Esteban Castro Sánchez --- Solvo
# 26.- Curso Python - Estructura Módulo
# python3

# Funciones basicas de una calculadora
# Si un archivo se va usar como modulo, se debe seguir un formato
# Formato de un modulo:
# 1. No debe de tener llamadas a funciones dentro del script,
#    solo crear funciones.
# 2. Indicar el interprete que se debe de utilizar al inicio.
# 3. Documentar todo el modulo.
# 4. Utilizacion de metadatas ; como por ejemplo, autor,email...

# Estructura de un modulo:
# 1. Interprete
# 2. Documentacion
# 3. Metadata
# 4. Funciones,objetos o variables

# Visualizar documentacion del modulo:
# 1. Ubicarse en la carpeta del proyecto en el terminal
# 2. Ingresar comando: python3
# 3. Ingresar comando: import "Nombre del modulo"
# 4. Ingresar comando: help("Nombre del modulo")
# 5. Ver atributos,algunos no colocados,
#    Ingresar comando: dir("Nombre del modulo")

"""
Funciones basicas de una calculadora
"""

__author__ = "Guillermo Castro Sanchez"
__copyright__ = "Copyright 2018, Solvo"
__credits__ = "Solvo"

__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Guillermo Castro Sanchez"
__email__ = "guillermoestebancs@gmail.com"
__status__ = "Junior Developer"


def suma(num1, num2):  # Suma
    """ Suma dos numeros """
    return num1+num2


def resta(num1, num2):  # Resta
    """ Resta dos numeros """
    return num1-num2


def multiplicacion(num1, num2):  # Multiplicacion
    """ Multiplica dos numeros """
    return num1*num2


def division(num1, num2):  # Division flotante
    """ Divide dos numeros con decimal"""
    return num1/num2


def division_entera(num1, num2):  # Division entera
    """ Divide dos numeros sin decimal"""
    return num1//num2


def porcentaje(num1, num2):  # Porcentaje
    """ Residuo de la division de dos numeros """
    return num1 % num2
