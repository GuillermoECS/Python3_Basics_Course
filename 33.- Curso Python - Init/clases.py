# Guillermo Esteban Castro Sánchez --- Solvo
# 33.- Curso Python - Init


class Lapiz:
    # Atributos: Caracteristicas de un objeto

    # Inicializador sin parametros, Constructor sin parametros
    """
    def __init__(self):
        self.color = "Amarillo"
        self.contiene_borrador = False
        self.usa_grafito = True
    """

    # Inicializador con parametros, Constructor con parametros
    '''
    def __init__(self, color, contiene_borrador, usa_grafito):
        self.color = color
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito
    '''

    # Inicializador con y sin parametros, Constructor con y sin parametros
    # Utiliza valores default si no hay parametros
    def __init__(self, color="Sin Color", contiene_borrador=False, usa_grafito=False):
        self.color = color
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito

    # Metodos: Acciones de un objeto, funciones

    def dibujar(self):  # La funcion debe ir identada
        # Metodo requiere la palabra self
        print("El lapiz esta dibujando")

    def borrar(self):
        # Siempre usar self para referirse a la clase
        if self.validar_borrar():
            # Los metodos siempre llevan () aunque no requieran parametros
            print("El lapiz esta borrando")
        else:
            print("No es posible borrar")

    def validar_borrar(self):
        # Siempre usar self para cosas referentes a la clase
        return self.contiene_borrador


# Las clases se instancian como si fueran funciones
# Sin parametros
lapiz_generico = Lapiz()
# Con parametros
# lapiz_generico = Lapiz("Verde", True, False)
lapiz_generico.dibujar()
lapiz_generico.borrar()
# Cambiar estado de un atributo
lapiz_generico.contiene_borrador = True
lapiz_generico.borrar()

# El metodo __init__ se crea cuando se ejecuta una instancia
