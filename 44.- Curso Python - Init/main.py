# Guillermo Esteban Castro Sánchez --- Solvo
# 44.- Curso Python - Init


# Uso del paquete
# No es la mejor forma de importar
# from animals.gato import Gato

# Para importar de la siguiente forma , requiere modificar __init.py__:
# from animals importa Gato


# Importar correctamente
from animals import Gato
from animals import creador_gatos
from animals import constante

gato = Gato("Gato de paquete")
print(gato.nombre)
gato = creador_gatos("Gato de __init__")
print(gato.nombre)
