#Ejercicio 1:Ordenar listas 
edad=[20,24,15,26,15,18,89]
edad.sort()
print(edad)

#Ejercicio 2:Ordenar listas descendente
edad.sort(reverse=True)
print(edad)

#Ejercicio 3: Ordenar y pasarlo a otra lista
edad2=[20,24,15,26,15,18,89]
edad_ascendente=sorted(edad2)
print(edad_ascendente)

#Ejercicio 5: Buscar datos en una lista y le devuelve  la posisicón en que se encuentra 
edad3=[12,15,14,18,61,12,16,13,18,19,20,24,45]
print(edad3.index(45))

#Ejercicio 6: verificar si un elemento está en lista
print(78 in edad3)


#Ejercicio 7: Insertar elementos en una lista
vegetales = ['espinaca','apio']
vegetales.insert(0,'lechuga')
print(vegetales)

#Ejercicio 8: agregar una elemento al final de una lista 
vegetales.append('esparrago')
print(vegetales)

#Ejercicio 9: Añadir mas elementos a lista
Precio = (10,15,8,30)
vegetales.extend(Precio)
print(vegetales) #Es lo mismo que concatenar dos listas

#Ejercicio 10: Borrar un elemento que esta en la lista
vegetales.remove('esparrago')
print(vegetales)

#Ejercicio 11: Para dejar una lista vacia
vegetales.clear()
print(vegetales)

# ['lechuga', 'espinaca', 'apio']
# ['lechuga', 'espinaca', 'apio', 'esparrago']
# ['lechuga', 'espinaca', 'apio', 'esparrago', 10, 15, 8, 30]
# ['lechuga', 'espinaca', 'apio', 10, 15, 8, 30]
# []


#Ejercicio 12: Contar elementos que se repoten en una lista
edades = [15, 21, 16, 19, 20, 16, 19, 15, 21, 17, 18]
print(edades.count(16))

for edad4 in range (15,25):
    print(f'La edad {edad4} se repite {edades.count(edad4)} veces')
    
