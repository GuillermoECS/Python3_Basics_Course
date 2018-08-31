# Guillermo Esteban Castro Sánchez --- Solvo
# 31.- Curso Python - Clases y Objetos

# Objeto: Entidad con caracteristicas y acciones
# Abstraer: Extraer las caracteristicas generales de un objeto, una plantilla
# Clase: Plantilla generica de un objeto, permiter crear N objetos
# En Python , todo es un objeto

# Clase lapiz
# Primer letra con mayuscula
# La convencion en el nombre de una clase es:
# Cada palabra con inicial mayuscula y seguidas sin guion bajo.


class Lapiz:
    # Requiere identacion
    # Atributos
    color = 'Amarillo'
    contiene_borrador = False
    usa_grafito = True

# Estructura de una clase
# Nombre de la clase
# Atributos
# Metodos


# Creacion de una instancia de una clase
lapiz_generico = Lapiz()
print(lapiz_generico.color)
print(lapiz_generico.contiene_borrador)
print(lapiz_generico.usa_grafito)
