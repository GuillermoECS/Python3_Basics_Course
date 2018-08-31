# Guillermo Esteban Castro Sánchez --- Solvo
# 43.- Curso Python - Paquetes

# Paquete : Folder o carpeta con los modulos requeridos
# Modulo: Archivos con extension .py , se debe agrupar por contexto
# Al agruparlos genera un paquete con un archivo init de extesion .py

# Creacion de un paquete:
# 1. Crear un folder con el nombre del paquete.
# 2. Agregar un archivo __ini__.py
# 3. Al menos un modulo
# Folder animals: Modulos correspondientes a animales.

# Uso del paquete
from animals.gato import Gato

gato = Gato("Gato de paquete")
print(gato.nombre)

# Se crea un folder (__pycache__) cuando mandamos a llamar un modulo
