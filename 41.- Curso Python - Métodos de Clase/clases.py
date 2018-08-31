# Guillermo Esteban Castro Sánchez --- Solvo
# 41.- Curso Python - Métodos de Clase

# Metodos de clase: Pertenecen a la clase
# Se pueden utilizar sin necesidad de objetos, como los estaticos


class Animal:
    volador = True


class Cocodrilo(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    # Metodos de clase: Son metodos estaticos que pueden utilizar todo lo
    # que este dentro de la clase (publico) y venga de la herencia (publico)
    # Utilizan un decorador y cls en vez de self
    @classmethod
    def new(cls, nombre):
        cls.volador = False
        return Cocodrilo(nombre)


cocodrilo = Cocodrilo.new('Coco')
print(cocodrilo.nombre)
