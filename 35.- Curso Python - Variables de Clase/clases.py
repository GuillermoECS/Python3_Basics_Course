# Guillermo Esteban Castro Sánchez --- Solvo
# 35.- Curso Python - Variables de Clase

# Clase circulo


class Circulo:
    # Variable de clase
    # Puede ser accedida directamente desde la clase
    # No requiere una instancia
    # No son inmutables, se puede modificar su valor
    # Propensa a cambios
    # Convencion para variables de clase : _
    _pi = 3.14
    # Constructor con parametros

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        # En la clase se usa self para acceder a los atributos
        # Inclusos las variables de clases
        return self.radio * self.radio * self._pi


instancia_circulo1 = Circulo(3)
instancia_circulo2 = Circulo(8)

# Areas
print(instancia_circulo1.area())
print(instancia_circulo2.area())

# Valor de Pi, se accede mediante la clase
print(Circulo._pi)

# Cambia el valor de Pi
Circulo._pi = 4.14
# Cambiar para las dos instancias
# Esta no es la forma correcta de acceder a Pi
print(instancia_circulo1._pi)
print(instancia_circulo2._pi)
