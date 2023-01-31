# Ejercicio1: Extraer elementos de una lista

potencias2=[2,4,8,16,32,64,128,264]
print(potencias2[3:5])
print(potencias2[:5])
print(potencias2[3:])
print(potencias2[:])
print(potencias2[::2])
print(potencias2[::-3])

#Ejercicio2: Cambiar elementos de una lista

potencias2[0:3]=['dos','cuatro','ocho']
print(potencias2[:])
print(id(potencias2))

#Ejercicio3: Poner valores vacios en la lista

potencias2[0:2]=[]
print(potencias2)

#Ejercicio4: Obtener un IDENTIFICADOR de la lista

print(id(potencias2))

#Ejercicio5: Borrar elementos de una lista (Del)

multiplos10= list(range(0,100,10))
print(multiplos10)

#borrar elelmentos desde la posición 3-6
del multiplos10[3:6]
print(multiplos10)

#borrar con un tamaño de paso
multiplos10_2 = list(range(0,100,10))
del multiplos10_2[::2]
print(multiplos10_2)

#borrar la lista completa
del multiplos10_2[:]
print(multiplos10_2)