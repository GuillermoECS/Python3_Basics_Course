# Guillermo Esteban Castro Sánchez --- Solvo
# 44.- Curso Python - Init

# Colocar todos los modulos que se quieran importar
# Punto:
# El interpretador de Python, busca el modulo gato
# al mismo nivel del archivo __init__.py
from .gato import Gato

# Tambien se puede generar la propia logica


constante = 0


def creador_gatos(nombre):
    return Gato(nombre)
