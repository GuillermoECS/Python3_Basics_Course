# Guillermo Esteban Castro Sánchez --- Solvo
# 29.- Curso Python - Argv

import sys

# Uso de parametros en un script .py
# Los parametros vienen separados por un espacio
# Imprime los parametros del script
# Si es el script principal
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'Nombre':
            print("Mi nombre es Guillermo")
        else:
            print(sys.argv)
    else:
        print("Indicar uno o mas parametros porfavor")

# Probar:
# Abrir terminal de comandos.
# Indicar comando: python3 "Nombre del script".py
# Ejemplos:
# python3 librerias.py #Sin parametros
# python3 librerias.py parametro1 parametro2 #Con parametros
