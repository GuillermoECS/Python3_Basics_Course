# Guillermo Esteban Castro Sánchez --- Solvo
# 20.- Curso Python - Funciones Anidadas


def validar_division_cero(numero1, numero2):  # Validar division entre cero
    return numero1 > 0 and numero2 > 0


def division_validada(numero1, numero2):  # Llamada de funciones
    if validar_division_cero(numero1, numero1):
        return numero1/numero2


# Uso de la funcion division validada
print(division_validada(6, 2))


# Funciones anidadas: Respetar identacion
def division_validada_anidada1(numero1, numero2):
    # Funcion anidada con parametro
    def validar_division_cero(numero1, numero2):  # Validar division entre cero
        return numero1 > 0 and numero2 > 0

    if(validar_division_cero(numero1, numero2)):
        return numero1/numero2


# Uso de la funcion division validada anidada con parametros
print(division_validada_anidada1(6, 2))


# Funcion anidada
def division_validada_anidada2(numero1, numero2):
    # Funcion anidada sin parametro
    def validar_division_cero():  # Validar division entre cero
        return numero1 > 0 and numero2 > 0

    if(validar_division_cero()):
        return numero1/numero2


# Uso de la funcion division validada anidada con parametros
print(division_validada_anidada2(6, 2))

# Puedo declarar funciones y no llamarlas


def crear_funcion_validar0(num1, num2):
    # Closure: Funcion que crear otra funcion
    # Funcion anidada sin parametro
    def validar_division_cero():  # Validar division entre cero
        return num1 > 0 and num2 > 0
    return validar_division_cero


# Usar funcion closure
validacion_cero = crear_funcion_validar0(8, 0)
print(validacion_cero())


def division_funcion_param(func):
    # Funcion con funcion en parametro
    print(func())


# Usar funcion con funcion en parametro
division_funcion_param(validacion_cero)
