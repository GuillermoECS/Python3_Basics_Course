# Guillermo Esteban Castro Sánchez --- Solvo
# 27.- Curso Python - Name

# Importar name del script calculadora
from calculadora import __name__ as __name__calculadora


# Todos los modulos son scripts, con extension .py
# Cada script tiene ciertos atributos
# El atributo __name__: Valor del script que se esta ejecutando
print(__name__)
print(__name__calculadora)

# Solo lo imprime si es el script principal en el que se trabaja
if __name__ == '__main__':
    print("Script principal", __name__)
