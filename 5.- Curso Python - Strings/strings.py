# Guillermo Esteban Castro Sánchez --- Solvo
# 5.- Curso Python - Strings

# Texto o cadena de caracteres
# String es una lista de caracteres, una union de caracteres
# String no se puede ver como un dato primitivo del todo
# Forma de declaracion #1
my_string = "Hola Mundo !"
print(my_string)
# Forma de declaracion #2
my_string = 'Hola Mundo'
print(my_string)
# Se puede usar comillas dentro de comillas simples y viceversa
my_string = 'Hola "Guillermo"'
print(my_string)
# Strings con saltos de linea declaracion #1
my_string = """Este es un String 
con saltos de linea"""
print(my_string)
# Strings con saltos de linea declaracion #2
my_string = '''Este es un String
con saltos de linea'''
print(my_string)
# Strings con saltos de linea en un reglon
my_string = '''Este es un String \ncon saltos de linea'''
print(my_string)
'''Strings al igual que enteros son inmutables,no pueden ser 
modificados solo se les puede agregar algo'''
course = 'Python 3'
name = 'Eduardo'
# Concatenacion de Strings #1
final_message = course+name
print(final_message)
# Concatenacion de Strings #2
final_message = 'Nuevo curso de '+course + ' por ' + name
print(final_message)
# Concatenacion de Strings #3
final_message = "Nuevo curso de %s por %s" % (course, name)
print(final_message)
# Concatenacion de Strings #4
# format es un metodo de la clase String
final_message = "Nuevo curso de {} por {}".format(course, name)
print(final_message)
