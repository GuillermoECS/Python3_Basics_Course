# Guillermo Esteban Castro Sánchez --- Solvo
# 36.- Curso Python - Properties

# Clase Usuario


class Usuario:
    # Constructor sin parametros
    def __init__(self, nombreUsuario, correo, contrasena):
        self.nombreUsuario = nombreUsuario
        self.correo = correo
        self.__contrasena = self.__mayuscula_contrasena(contrasena)  # privado

    # Contrasena en mayuscula , privado
    def __mayuscula_contrasena(self, contrasena):
        return contrasena.upper()

    # Get de la contrasena : Acceder atributo privada
    def get_contrasena(self):
        return self.__contrasena

    # Getter para acceder a atributos privados
    # Decorador para acceder atributo,no permite modificar
    # Nombrarlo igual al atributo
    @property
    def contrasena(self):
        return self.__contrasena

    # Setter para modificar atributos privados
    # Decorador para acceder atributo + Decorador para modificar atributo

    @contrasena.setter
    def contrasena(self, valor):
        self.__contrasena = valor


usuario_personal = Usuario("Guillermo", "guillermo@gmail.com", '123')
print("Usuario ", usuario_personal.nombreUsuario)
print("Correo ", usuario_personal.correo)
print("Contrasena ", usuario_personal.get_contrasena())

# Modificacion de atributo privado
usuario_personal.contrasena = "nueva contrasena"
print(usuario_personal.contrasena)
