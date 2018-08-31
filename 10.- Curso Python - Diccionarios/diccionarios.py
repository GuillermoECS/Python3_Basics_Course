# Guillermo Esteban Castro Sánchez --- Solvo
# 10.- Curso Python - Diccionarios

# Diccionarios: Estructuras de datos para almacenar diferentes tipos de datos.
# No se rige por un indice, utiliza llaves o claves que pueden ser
# enteros, caracteres...
# Las claves deben de ser inmutables
# Las claves pueden ser numeros , caracteres, tuplas, etc
diccionario = {'a': True, 5: "Esto es un string", (1, 2): False}
print(diccionario)
# Si existen llaves iguales, la llave se queda con el ultimo valor asignado
diccionario = {'a': True, 'a': "Esto es un string", (1, 2): False}
print(diccionario)
# Los diccionarios pueden cambiar su tamano, agregar
# nuevo registro en el diccionario
diccionario['c'] = 'nuevo registro'  # Agregar registro (clave,valor)
print(diccionario)
# Modificar registro del diccionario
diccionario[(1, 2)] = True
print(diccionario)
# Obtener datos del dicccionario
# Obtener valor del diccionario en 'a'
valor = diccionario['a']  # Si no existe la llave va dar error
print(valor)
# Obtener valor del diccionario, controlar el error si no existe la llave
# Puede regresar el valor que desee si no encuentra la clave
valor = diccionario.get('z', 'no existe')
print(valor)
# Eliminar llave del diccionario
del diccionario['c']
print(diccionario)
# Obtener llaves del diccionario
llaves = diccionario.keys()  # Objeto iterable
print(llaves)
# Convertir llaves del diccionario en una lista
llaves = list(llaves)
print(llaves)
# Obtener valores del diccionario
valores = diccionario.values()  # Objeto iterable
print(valores)
# Convertir valores del diccionario en una lista
valores = list(valores)
print(valores)
# Convertir valores del diccionario en una tupla
valores = tuple(valores)
print(valores)
# Agregar registros de un diccionario a otro diccionario forma #1
diccionario2 = {'w': 23, (1, 4): 'wwwwwe'}
diccionario['w'] = diccionario2['w']
diccionario[(1, 4)] = diccionario2[(1, 4)]
print(diccionario)
# Agregar registros de un diccionario a otro diccionario forma #2
diccionario.update(diccionario)
print(diccionario)
