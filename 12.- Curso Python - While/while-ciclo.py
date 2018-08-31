# Guillermo Esteban Castro Sánchez --- Solvo
# 12.- Curso Python - While

# While: Cuando no se este seguro cuantos ciclos realizar
# Estructura:
# While condicion:
#    codigo
# Estructura con else:
# While condicion:
#    codigo
# else # Cuando la condicion no se cumpla
#    codigo

# Forma #1 con contador
contador = 0
while contador < 10:  # > < >= <= == != 
    print(contador)
    contador = contador + 1  # contador +=1
    if contador == 5:
        print("El contador es ", contador)
        print("Continue contando")
        continue  # Continue el ciclo
    elif contador == 8:
        print("El contador es ", contador)
        print("Rompa el ciclo")
        break
else:
    print('Ya no se cumple el ciclo')

# Forma #2 con bandera, mas elegante
contador = 0
bandera = True
while bandera:
    print(contador)
    contador = contador + 1  # contador +=1
    if contador == 5:
        print("El contador es ", contador)
        print("Continue contando")
        continue  # Continue el ciclo
    elif contador == 8:
        print("El contador es ", contador)
        print("Rompa el ciclo")
        bandera = False
else:
    print('Ya no se cumple el ciclo')
