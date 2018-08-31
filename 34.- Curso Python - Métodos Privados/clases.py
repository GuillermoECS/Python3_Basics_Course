# Guillermo Esteban Castro Sánchez --- Solvo
# 34.- Curso Python - Métodos Privados

# Clase con atributos y metodos privados


class Usuario:
    # Siempre usar palabra self en parametros del metodo
    # Y al inicio de atributos
    def __init__(self, nombre_user, corr, contra):
        self.nombre_usuario = nombre_user
        self.correo = corr
        self.__contrasena = contra  # atributo privado : al inicio poner __

    # Obtener variable privada
    def get_contrasena(self):  # Obtener atributo privado
        return self.__contrasena

    # metodo privado:al inicio poner __
    def __cambiar_contrasena(self, contrasena):
        return self.__contrasena.upper()


guillermo = Usuario("Memo", "memo@gmail.com", 123)
# print(guillermo.__contrasena)
guillermo.nombre_usuario = "Guillermo"
guillermo.correo = "guillermo@gmail.com"
print(guillermo.nombre_usuario)
print(guillermo.correo)
try:
    print(guillermo.__contrasena)
except Exception as error:
    print("Errror", error)


# Los metodos y atributos privados solo van a poder ser accedidos
# dentro de la clase y no por la instancia.

# El atributo esta oculto (privado), pero yo puedo crear uno nuevo
# con el mismo nombre, no afecta el de la clase
guillermo.__contrasena = 233434
guillermo.__contrasena = 222
print("Contrasena real", guillermo.get_contrasena())
print("Contrasena con mismo nombre de atributo", guillermo.__contrasena)
