# Guillermo Esteban Castro Sánchez --- Solvo
# 18.- Curso Python - Argumentos

# Funcion con N cantidad de argumentos por medio de tuplas
# * -> Indica que puede recibir N argumentos


def mostrar_valores(*argumentos):
    print(argumentos)
    # Identificar tipo de una variable
    print(type(argumentos))


# Uso de la funcion
mostrar_valores(4, 5, 7)  # Obtiene los argumentos y los convierte en una tupla
# Uso de la funcion sin parametros
mostrar_valores()


# Funcion de suma de N de parametros
# Los argumentos con * al inicio se les llama args normalmente
def suma_argumentos(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado


# Uso de la funcion suma de argumentos
print(suma_argumentos(1, 2, 3, 4, 5, 6, 7, 8, 9))


# Funcion con N cantidad de argumentos por medio de diccionario
# ** -> Puede recibir N cantidad de parametros , indicando el valor de cada uno
# ** -> Se les llama Kwargs
def mostrar_valores_dic(**kwargs):
    valor = kwargs.get("valor", "No existe la llave o clave indicada")
    print(valor)


# Uso de la funcion
mostrar_valores_dic(valor=4, uno="uno", verdadero=True)

# * -> N valores -> tupla
# ** -> N valores -> diccionario
