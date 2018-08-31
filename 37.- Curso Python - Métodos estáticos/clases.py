# Guillermo Esteban Castro Sánchez --- Solvo
# 37.- Curso Python - Métodos estáticos

# Clase Circulo


class Circulo:
    # Variable de la clase
    pi = 3.1416

    # Metodo estatico: No usa la palabra self
    # Usa un decorador
    # Uso de este tipo de metodos : Algo que no cambie

    @staticmethod
    def get_pi_value():
        return 3.14

    # Constructor sin parametros
    def __init__(self, radio):
        self.radio = radio

    # Metodo de estancia: funcion en una clase, usa la palabra self
    # Metodo de instancia, usa la palabra self
    # Calcular area
    def area(self):
        return self.radio * self.radio * self.pi
        # Otra forma con metodo estatico
        # return self.radio * self.radio * self.get_pi_value()


circulo_uno = Circulo(4)
# Metodo de instancia
print("Area", circulo_uno.area())
# Metodo estatico
print("Valor de Pi", Circulo.get_pi_value())
