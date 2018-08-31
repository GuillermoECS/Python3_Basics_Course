# Guillermo Esteban Castro Sánchez --- Solvo
# 21.- Curso Python - Decoradores

# A, B y C son funciones
# A recibe como parametro B para poder crear C
# Un decorador es una funcion que recibe otra funcion para
# agregarle funcionalidades, decora la funcion,
# creando asi una nueva funcion.

# A: La funcion que se encarga de agregar mas funcionalidades , Wrapper
# B: La funciona a la que se le quiere agregar funcionalidades
# C: La nueva funcion, la funcion con nuevas funcionalidades


def decorador1(func):  # A

    # Decorador sin parametros en la funcion B
    def nueva_funcion1():  # B
        print("Antes de saludar")
        func()
        print("Despues de saludar")
    return nueva_funcion1  # C


@decorador1
def funcion_decorada_sin_param():
    print("Hola mundo")


# Uso de la funcion decorada sin parametros
funcion_decorada_sin_param()


def decorador2(func):  # A

    # Decorador con parametros en la funcion B
    def nueva_funcion2(*args, **kwargs):  # B
        print("Multiplicacion y Suma")
        resultado = args[0] * func(*args, **kwargs)
        return resultado
    return nueva_funcion2  # C


@decorador2
def funcion_decorada_con_param(numero1, numero2):
    return numero1+numero2


# Uso de la funcion decorada con parametros
print(funcion_decorada_con_param(4, 5))


def decorador_con_dos_funciones(func):  # Decorador con dos funciones
    def before_action():
        print("Antes del saludo")

    def after_action():
        print("Despues del saludo")

    def nueva_funcion3():
        before_action()
        func()
        after_action()
    return nueva_funcion3


@decorador_con_dos_funciones
def saludo_con_decorador_dos_funciones():
    print("Hola mundo!")


# Uso de la funcion
saludo_con_decorador_dos_funciones()


# Decorador con parametros
# Requiere dos decoradores
# 1. Decorador para la funcion
# 2. Decorador para el parametro del decorador
def decorador_con_parametros(is_valid):
    def decorador_funciones(func):  # Decorador con dos funciones
        def before_action():
            if is_valid:
                print("Antes del saludo")

        def after_action():
            print("Despues del saludo")

        def nueva_funcion4():
            before_action()
            func()
            after_action()
        return nueva_funcion4
    return decorador_funciones


@decorador_con_parametros(False)
def saludo_con_decorador_parametros():
    print("Hola mundo!")


# Uso de la funcion decorador con parametros
saludo_con_decorador_parametros()
