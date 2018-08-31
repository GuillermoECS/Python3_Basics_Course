# Guillermo Esteban Castro Sánchez --- Solvo
# 24.- Curso Python - Módulos

# Modularizar: Separar el codigo en contextos.
# Modulos: Archivos con extensiones .py para ser utilizados dentro
# de otros archivos.
# Colocar los dos archivos a un mismo nivel


# Importar achivos al mismo nivel:
# Solo escribir import "Nombre del archivo"
import calculadora

resultado = calculadora.suma(33, 444)
print(resultado)

# Carpeta __pycache__:
# Contiene el archivo compilado de los modulos, mejora performance
# Si existe lo utiliza; de no ser asi, lo crea
# El script es mas rapido , utiliza el compilado y no interpretado
