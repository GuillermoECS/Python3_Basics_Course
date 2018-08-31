# Guillermo Esteban Castro Sánchez --- Solvo
# 23.- Curso Python - Docstring


def generador(*args):

    # Documentacion de una funcion
    # Siempre colocar la documentacion en la primera linea,
    # No arriba de la funcion
    """ Aqui va todo lo que hace la funcion
 Ejemplo: Recibe n cantidad de numeros y regresa el numero
 ademas de regresar True o False si el numero es mayor a 5
    """
    for valor in args:
        yield valor, True if valor > 5 else False


# En Python las funciones son clases
# ._doc_ es un atributo, muestra la documentacion
nombre = generador.__name__
documentacion = generador.__doc__
print(nombre, ":")
print(documentacion)

# Guardar la documentacion de una funcion:
# 1. Abril terminal de comandos de python3
# 2. Ingresar el comando: from func importa "Nombre de la funcion de la que se quiere la documentacion"

# Obtener ayuda de la funcion guardada
# 1. Abril terminal de comandos de python3
# 2. Ingresar el comando: help ("Nombre de la funcion de la que se quiere la documentacion")

# Siempre documentar el codigo , es una buena practica
