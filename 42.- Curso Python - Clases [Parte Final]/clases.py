# Guillermo Esteban Castro Sánchez --- Solvo
# 42.- Curso Python - Clases [Parte Final]


class Usuario:
    def __init__(self, password):
        print("Este metodo se ejecuta segundo")
        self.__password = password  # Privado, solo se usa en la clase

    # Metodo magico : Metodo predefinido
    # def __new__(cls):
    #    print("Este metodo se ejecuta primero")
    #    return super().__new__(cls)

    # Metodo magico
    # Sustituir lo que imprime print(Nombre del objeto)
    def __str__(self):
        return "Passsword : " + self.__password

    # Metodo magico
    # Cuando no se encuentra algun atributo
    def __getattr__(self, nombre_atributo):
        print("No se encontro el atributo")


usuario_prueba = Usuario('567')
# Se pueden crear atributos a los objetos
print(usuario_prueba.__dict__)
usuario_prueba.nombre = "Guillermo"
print(usuario_prueba.__dict__)
print(usuario_prueba.nombre)

# Crear un atributo con el mismo nombre al atributo privado
# Pero es diferente , uno es publico y otro es privado
# El privado lleva la palabra "_Usuario"
print(usuario_prueba.__dict__)
usuario_prueba.__password = '123'
print(usuario_prueba.__password)
print(usuario_prueba.__dict__)
# Metodo print modificado por __str__
print(usuario_prueba)
# No se encuentra el atributo apellidos
usuario_prueba.apellido
