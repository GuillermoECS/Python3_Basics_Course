# Guillermo Esteban Castro Sánchez --- Solvo
# 30.- Curso Python - Excepciones

# Excepcion: Errores que se presentan dentro del script cuando se ejecuta
# Se deben realizar, para evitar que se caiga de forma abrupta
# Es importante visualizar donde ocurren los errores

# Manejo de excepcion #1: Division entre cero
division = 0
try:  # Lanza el error si ocurre,se intenta ejecutar
    division = 5/0  # Codigo que podria caerse
    # as : Indicar alias para conocer tipo de error
except ZeroDivisionError as ex:  # Atrapa error, indicar tipo
    print("Error tipo: ", ex)  # Siempre indica el error , para estar seguros
    print("No se permite la division entre cero")
print("Finalizo el script")

# Manejo de excepcion #1: Elemento fuera de la lista
division = 0
try:  # Lanza el error si ocurre, se intenta ejecutar
    lista = [1, 2]
    print(lista[2])
except IndexError as error:  # Atrapa error, indicar tipo
    print("Error tipo: ", error)  # Siempre indicar el error
    print("No es posible obtener valor 2")
# Se pueden colocar varios except, para los errores posibles
except ZeroDivisionError as ex:  # Atrapa error, indicar tipo
    print("Error tipo: ", ex)  # Siempre indica el error , para estar seguros
    print("No se permite la division entre cero")
print("Finalizo el script")

# Manejo de excepciones #3 : Cualquier tipo de error
# Tratar de investigar siempre e indicar el error
division = 0
try:  # Lanza el error si ocurre, se intenta ejecutar
    lista = [1, 2]
    print(lista[2])
except Exception as error:
    print("Error tipo ", error)
print("Finalizo el script")

# Manejo de excepciones #4 :
# Agregando bloque que siempre se ejecuta, finally
division = 0
try:  # Lanza el error si ocurre, se intenta ejecutar
    lista = [1, 2]
    print(lista[2])
except Exception as error:  # Solo si hay error
    print("Error tipo ", error)
finally:  # Siempre se ejecuta, Si o Si
    print("Siempre se muestra")
print("Finalizo el script")
