# Guillermo Esteban Castro Sánchez --- Solvo
# 45.- Curso Python - SubPaquetes


# Uso del paquete
# No es la mejor forma de importar
# from animals.gato import Gato

# Para importar de la siguiente forma , requiere modificar __init.py__:
# from animals importa Gato


# Importar correctamente
from animals import Gato

gato = Gato("Gato de paquete")
print(gato.nombre)
# Usar funcion heredada
print(gato.comer())
