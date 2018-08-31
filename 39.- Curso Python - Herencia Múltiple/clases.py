# Guillermo Esteban Castro Sánchez --- Solvo
# 39.- Curso Python - Herencia Múltiple

# Herencia Multiple: Heredar de N
# Ocultar codigo, presionar en flecha (-) en el lado izquierdo


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


class Mascosta(Animal):  # Clase Padre de Mascota
    nombre = ''

    def llamar_mascota(self):
        print(self.nombre)


class Gato (Felino, Mascosta):
    # Clase hija, Hereda de la clase Mascosta Felino y Animal
    def cazador(self):
        print(self.cazar())


class Jaguar (Felino):  # Clase hija, Hereda de la clase Felino y Animal
    pass


# Uso de las clases hijas
gato = Gato()
jaguar = Jaguar()

# Pueden utilizar properties, atributos y metodos de la clase hija Publicos
print(gato.animal_terrestre)
jaguar.cazar()

# Utilizar la herencia multiple
gato.nombre = "Gato con botas"
gato.llamar_mascota()
