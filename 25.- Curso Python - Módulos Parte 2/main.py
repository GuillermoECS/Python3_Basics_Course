# Guillermo Esteban Castro Sánchez --- Solvo
# 25.- Curso Python - Módulos Parte 2

# Formas de importar funciones especificas,
# no todo el modulo
from calculadora import suma as sum  # 1 , Alias
from calculadora import resta, multiplicacion  # 2, Sin alias
from calculadora import (division, division_entera)  # 3, con parentesis
from calculadora import *  # 4 , importar todo

# Ya no es necesario indicar la pertenencia a la calculadora
resultado = sum(33, 444)
print(resultado)
resultado = multiplicacion(33, 444)
print(resultado)
