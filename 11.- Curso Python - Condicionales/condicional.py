# Guillermo Esteban Castro Sánchez --- Solvo
# 11.- Curso Python - Condicionales

fruta = 'Manzana'
# Estrucutra de un condicional
# if condicion :
#   codigo
# = -> Asignacion
# == ->Comparacion
# Forma #1 Condicional
if fruta == "kiwis":  # Si y solo si
    print("La fruta es un Kiwi")
elif fruta == "Manzana":
    print("La fruta es una manzana")
elif fruta == "Pera":  # Se pueden tener N cantidad de elif
    print("La fruta es una Pera")
else:
    print("No es un Kiwi")
# Forma #2 Condicional
mensaje = 'La fruta es un Kiwi' if fruta == 'kiwi' else 'No son iguales'
print(mensaje)
mensaje = True if fruta == 'kiwi' else 'No son iguales'
print(mensaje)
# Si queremos que un codigo se ejecute dentro de un if,elif,else...
# Siempre debe de ir identado
# Al realizar un if,elif,else...
# Si se quiere que no se haga nada usar pass
if fruta == "Naranaja":
    pass
# Tipos de condiciones: >,<,>=,<=,==,!=
if fruta != "Naranja":
    print("No es una naranja")
# True = 1, False =0
if True:
    print("Verdadero")
elif False:
    print("Falso")
if 1:
    print("Verdadero")
elif 0:
    print("Falso")
# Todas las variables que se encuentren vacias o nulas van a ser falsas
if []:  # 0, [],{},(),'',""
    print("Verdadero")
else:
    print("Falso")
# None, quiere decir que no tiene ningun valor
variable_sin_valor = None
if variable_sin_valor:
    print("Con valor")
else:
    print("Sin valor")
# Condicional and: Se deben cumplir todos
if variable_sin_valor is None and fruta == 'Manzana':
    print("Sin valor")
else:
    print("Con valor")
# Condicional or: Se debe cumplir alguno
if variable_sin_valor is None and fruta == 'Manzana':
    print("Sin valor")
else:
    print("Con valor")
