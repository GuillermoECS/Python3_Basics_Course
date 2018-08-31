# Guillermo Esteban Castro Sánchez --- Solvo
# 28.- Curso Python - Librerías

# Python permite trabajar con librerias predefinidas
import random
import datetime
import sys
import time


# RANDOM:
valor_aleatorio = random.randint(0, 10)  # de 0 a 10
print(valor_aleatorio)

# Lista con valores
lista = [1, 2, True, (1, 2), "Hola"]
valor = random.choice(lista)  # Valor random de la lista
print(valor)

# Desordenar lista
print(lista)
random.shuffle(lista)
print(lista)


# DATETIME:
print(datetime.datetime.now())


# SYS:
# Barra de progreso con SYS
for i in range(101):
    time.sleep(0.5)  # Duerma medio segundo
    #  Imprima en la misma posicion del terminal
    #  Dos porcentajes porque no se quiere concatenar dos valores
    #  Mas bien , agregar uno , un %
    sys.stdout.write("\r%d %%" % i)
    # sys.stdout.write("Progreso")  # Escribir
    sys.stdout.flush()  # Mostrar
