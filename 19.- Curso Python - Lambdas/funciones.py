# Guillermo Esteban Castro Sánchez --- Solvo
# 19.- Curso Python - Lambdas

# Lambda: Permite la creacion de pequenas funciones anonimas
# en una linea de codigo.
# Se mandan a llamar dependiendo de las condiciones del programa
# No se utilizan ciclos, ni condicionales
# Todo debe ser en una linea de codigo
# Lambda siempre regresa algo, no requiere return


# Funcion lambda de suma
funcion_suma = lambda valor1, valor2: valor1+valor2
# Uso de la funcion lambda
print(funcion_suma(1, 3))


# Funcion lambda formato de pregunta
funcion_formato_pregunta = lambda sentencia: '{}?'.format(sentencia)
# Uso de la funcion lambda
print(funcion_formato_pregunta("Hola, que hace"))

# Funcion lambda no retorna nada pero hace una accion
funcion_no_hace_nada = lambda : print("No hago nada")
# Uso de la funcion lambda
# Si no regresa algo retorna None, debe de tener un accion
print(funcion_no_hace_nada())
