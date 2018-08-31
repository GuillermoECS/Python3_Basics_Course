# Guillermo Esteban Castro Sánchez --- Solvo
# 13.- Curso Python - For

# For: Permite iterar objetos iterables ;como por ejemplo, listas,
# diccionarios,tuplas,strings,...
# lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for valor in lista:
    # print(valor)
    pass
# tupla
lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for valor in lista:
    # print(valor)
    pass
# Objeto iterable range de 10 a 19, dos parametros
# Primer parametro: donde comienza
# Segundo parametro: donde termina sin contarlo
rango = range(10, 20)
for valor in rango:
    # print(valor)
    pass
# Objeto iterable range de 0 a 17, un parametro
rango = range(18)
for valor in rango:
    # print(valor)
    pass
# Objeto iterable rango de 0 a 24, tres parametros
# Tercer parametro: Salto
rango = range(0, 25, 3)
for valor in rango:
    # print(valor)
    pass
# For en otros lenguajes
# for(int i=0;i<25;i++)
for valor in range(0, 25, 1):
    # print(valor)
    pass
# Determinar indice de una lista
indice = 0
for valor in lista:
    # print("Indice ", indice, ",Valor ", valor)
    pass
    indice += 1
# Funciones en Python permiten regresar N cantidad de valores
# Enumerate regresa N cantidad de valores
for indice, valor in enumerate(lista):
    # print("Indice ", indice, ",Valor ", valor)
    pass
# len regresa el tamano de cualquier objeto iterable
for valor in range(0, len(lista)):
    # print(valor)
    pass
# Los Strings son iterables, los numeros no
for valor in 'Guillermo':
    # print(valor)
    pass
# Los diccionarios son iterables
# diccionario.keys() : llaves o claves del diccionario
# diccionario.values() : Valores del diccionario
# diccionario.items() : Llaves y valores del diccionario
diccionario = {'a': 10, 33: 22, (1, 2): "aa"}
for llave, valor in diccionario.items():
    print("Llave ", llave, ",Valor ", valor)
# Se puede iterar diversas estructuras , a excepcion de los numeros
