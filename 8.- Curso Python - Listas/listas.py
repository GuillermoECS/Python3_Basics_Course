# Guillermo Esteban Castro Sánchez --- Solvo
# 8.- Curso Python - Listas

# Listas: Pueden almacenar diferentes tipos de datos ; como por ejemplo,
# strings, numeros booleanos
# A diferencia de los Strings y enteros, pueden modificar su tamano
# Las listas utilizan parentesis cuadrado
my_list = ["strings", 15, 15.7, True]
print(my_list)
# Las listas pueden crecer y decrecer, se leen de izquierda a derecha
my_list.append(6)  # Agrega el elemento en la ultima posicion
print(my_list)
my_list.insert(1, "insert")  # Indicar la posicion y el valor a ingresar
print(my_list)
# Todo lo respectivo a Strings se encuentra tambien en listas
# Mostrar elemento en posicion 0
print(my_list[0])
# Borrar el elemento 15 , es diferente a 15.6
my_list.remove(15)
print(my_list)
# Las listas se pueden manipular como un stack
my_list.pop()  # Extrae el ultimo elemento de la lista
print(my_list)

# Lista de enteros
my_number_list = [1, 6, 77, 8, 2, 3, 4, 55, 66, 67]
print(my_number_list)
# Ordena la lista ascendentemente, de menor a mayor
my_number_list.sort()
print(my_number_list)
# Ordena la lista descendentemente, de mayor a menor
my_number_list.sort(reverse=True)
print(my_number_list)
# Unir dos listas de diferentes tipos
# extend = unir dos listas
my_list.extend(my_number_list)
print(my_list)
# Unir dos listas del mismo tipo
my_number_list2 = [2, 4, 5, 6, 7, 8, 1, 2, 34]
my_number_list.extend(my_number_list2)
print(my_number_list)
# Append = Agregar elemento en una lista
my_number_list.append(my_number_list2)
print(my_number_list)
