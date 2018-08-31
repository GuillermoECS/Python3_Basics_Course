# Guillermo Esteban Castro Sánchez --- Solvo
# 27.- Curso Python - Name
# python3

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


def saluda():  # Saluda
    print("Hola a todos!")


if(__name__ == '__main__'):  # Solo saluda si se encuentra en el main principal
    saluda()
