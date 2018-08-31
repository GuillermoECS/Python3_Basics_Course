# Guillermo Esteban Castro Sánchez --- Solvo
# 32.- Curso Python - Atributos y Métodos


class Lapiz:
    # Atributos: Caracteristicas de un objeto
    color = 'Amarillo'
    contiene_borrador = False
    usa_grafito = True
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
lapiz_generico = Lapiz()
lapiz_generico.dibujar()
lapiz_generico.borrar()
# Cambiar estado de un atributo
lapiz_generico.contiene_borrador = True
lapiz_generico.borrar()
