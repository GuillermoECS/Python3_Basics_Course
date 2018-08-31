# Guillermo Esteban Castro Sánchez --- Solvo
# 22.- Curso Python - Generadores

# Generadores son para crear objeto sin necesidad de almacenarlos en memoria RAM
# enumerate y range son generadores
# Por lo general , utilizan un loop

# NO funciona, porquen no se puede iterar con un return


def generador_invalido(*args):  # Generador propio
    for valor in args:
        return valor * 10  # Ejemplo


def generador_valido(*args):  # Generador propio
    for valor in args:
        yield valor * 10, True  # Ejemplo


for valor1, valor2 in generador_valido(1, 2, 3, 4, 5, 6, 7, 8, 9):
    print(valor1, valor2)
