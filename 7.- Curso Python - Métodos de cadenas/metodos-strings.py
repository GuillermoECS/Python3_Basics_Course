# Guillermo Esteban Castro Sánchez --- Solvo
# 7. - Curso Python - Métodos de cadenas

'''Metodos de formato'''
course = 'Curso'
my_string = 'Codigo Facilito!'
# Concatenar valores de dos variables
result = '{} de {}'.format(course, my_string)
print(result)
# Concatenar valores de dos variables mediante un alias, a y b, para formato
# a los strings
result = '{a} de {b}'.format(b=course, a=my_string)
print(result)
# Convertir en minuscula todos los caracteres, no se guarda en la variable solo
# si yo se lo indico
result = result.lower()
print(result)
# Convertir en mayuscula todos los caracteres, se guarda en la variable solo
# si yo se lo indico
result = result.upper()
print(result)
# Poner un String como un titulo, cada palabra inicia en Mayuscula
result = result.title()
print(result)

'''Metodos de busqueda '''
# Encontrar la posicion en donde inicia una palabra o caracter
# Es sensible a mayusculas, minusculas y acentos
pos = result.find('Codigo')
print(pos)
print(result[pos:6])
# Contar numero de veces que se encuentra una palabra o caracter
count = result.count('!')
print(count)
# Remplazar un caracter por otro caracter
result = result.replace('C', '@')
print(result)
# Separa un conjunto de caracteres de acuerdo al caracter indicado
# en una lista
result = result.split(' ')
print(result)
print(result[0])
