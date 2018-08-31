# Guillermo Esteban Castro Sánchez --- Solvo
# 6.- Curso Python - Strings como listas

my_string = 'curso de Codigo Facilito!'
print(my_string)
# Funcionamiento de los caracteres en el string anterior
# C U R S O
# 0 1 2 3 4
# Manejar el String caracter por caracter
print(my_string[0])
print(my_string[1])
# Los espacios cuentan como caracteres
print(my_string[5])
# Imprimir empezando el ultimo caracter, sin necesidad de contar
# los caracteres
print(my_string[-1])
# Imprimir el penultimo caracter
print(my_string[-2])
# Imprimir cantidad de digitos desde cierta posicion
# Genera un substring desde la posicion 0 hasta la posicion 9
print(my_string[0:15])
# Imprimir el penultimo digitos
print(my_string[-2:-1])
# Mostrar los caracteres hasta la posicion #10, mostrar de dos en dos
# Cuenta el caracter en el que esta
print(my_string[0:10:2])
# print(my_string[caracter donde inicia:caracter donde se detiene:
# cada cuanto lo muestra])
# Mostrar String de forma reversa
print(my_string[::-1])
