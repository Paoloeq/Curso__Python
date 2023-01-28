# Ejercicio 1: Crear una tupla
tupla=()
print(len(tupla))

# Ejercicio 2: Crear una tupla con elementos
tupla2=('hola','como','estas')
print(len(tupla2))

# Ejercicio 3: Llamar elementos de una tupla
print(tupla2[1],'se llama para decirle ',tupla2[0])

# Ejercicio 4: Listas dentro de una tupla y asignar variables a elementsode una tupla
datos_Paciente=('Paolo',[27,54])
nombre,edad_peso = datos_Paciente;

print(nombre)
print(edad_peso)

estatura, peso , temperatura =(1.5,64,20)
print(f'{estatura}-{peso}-{temperatura}')

# Ejercicio 5: Tuplas dentro de una listas - Enumerar elementos (indices)

nombres=('Paolo','Marlon','Mario')
lista_nombres=list(enumerate(nombres))
tupla_nombres=tuple(enumerate(nombres))

print(lista_nombres)
print(tupla_nombres)

for indice,valor in enumerate(nombres):
    print(f'{indice}:{valor}')

import numpy as np
