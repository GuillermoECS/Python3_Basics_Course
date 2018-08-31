# Guillermo Esteban Castro Sánchez --- Solvo
# 45.- Curso Python - SubPaquetes

# Clase Hija de Animal
# Importar clase animal
# . -> Buscar al mismo nivel
# .. -> Buscar un nivel arriba

from ..animal import Animal


class Gato(Animal):
    def __init__(self, nombre):
        self.nombre = nombre
