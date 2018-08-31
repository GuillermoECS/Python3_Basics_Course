# Guillermo Esteban Castro Sánchez --- Solvo
# 40.- Curso Python - Override


class Animal:  # Clase Padre Animal
    # Hereda sus atributos, metodos y properties PUBLICOS
    @property
    def animal_terrestre(self):
        return True


class Felino(Animal):  # Clase Hija de Animal, clase Padre de Gato y Jaguar
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino esta cazando")


class Mascota(Animal):  # Clase Padre de Mascota
    # nombre = ''

    def __init__(self, nombre):
        self.nombre = nombre

    def llamar_mascota(self):
        print(self.nombre)


class Gato (Felino, Mascota):
    # Clase hija, Hereda de la clase Mascosta, Felino y Animal

    # Constructor de la clase Gato, usando constructor Padre
    def __init__(self, nombre, raza):
        Mascota.__init__(self, nombre)
        self.raza = raza

    def cazador(self):
        print(self.cazar())
    # Override : Sobreescritura de Metodos, el metodo se debe llamar igual
    # Tomar un metodo y cambiarle el comportamiento
    # Primero lo busca en la clase donde se llama , luego en la primera clase
    # heredada y asi sucesivamente. Si no lo encuentra , indica error

    def llamar_mascota(self):
        # Utilizar metodo de la clase padre:
        Mascota.llamar_mascota(self)
        print("El nombre de la mascota es : {}".format(self.nombre))


class Jaguar (Felino):  # Clase hija, Hereda de la clase Felino y Animal
    pass


# Uso de las clase gato con metodos Override
gato = Gato("Gato con botas", "Blanco")
gato.llamar_mascota()
print(gato.raza)
