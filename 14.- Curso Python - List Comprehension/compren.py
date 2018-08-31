# Guillermo Esteban Castro Sánchez --- Solvo
# 14.- Curso Python - List Comprehension

# Lista con numeros del 1 al 100
lista_numeros = []  # False
for valor in range(0, 101):
    lista_numeros.append(valor)
# print(lista_numeros)
# Crear lista mediante list comprehension
lista_numeros = [valor for valor in range(0, 101)]
# print(lista_numeros)
lista_numeros = ["value" for valor in range(0, 101)]
# print(lista_numeros)
# Reglas de List Comprehension:
# 1.Debe existir un valor.
# 2.Un ciclo, for.
# 3.Opcional: Condicion.
# Unicamente permitir numeros pares
lista_numeros = [valor for valor in range(1, 51) if valor % 2 == 0]
# print(lista_numeros)
# Crear tupla mediante list comprehension
tupla_impares = tuple([valor for valor in range(1, 51) if valor % 2 != 0])
print(tupla_impares)
# Crear diccionario mediante list comprehension
diccionario_numeros = {llave: valor for llave,
                       valor in enumerate(lista_numeros) if llave < 30}
print(diccionario_numeros)
