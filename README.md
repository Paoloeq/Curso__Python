# Curso de Python para data Scientist
## Clase 1: Sentencia if
```py
nac=1999
if 2021-nac>=25:
    print("posible cliente")
```
## Clase 2: Listas 
Una lista se declara en **CORCHETES** 

`A=[1,2,3,4,5] `

`B=["maria",'Rodriguez']`

Hacer una llamado a un elemento de la lista
`A[4]`

Ver Longitud del la lista
`len(A)`

Añadir elementso en una lista vacia DINAMICA
```py
mi_secuencia=[]
for número in range(-2,3):
    mi_secuencia += [número]
    
print(mi_secuencia)

#[-2, -1, 0, 1, 2]
```
Partir letra por letra a un palabra
```py
letras =[]
letras += 'Comida'

print(letras)

#['C', 'o', 'm', 'i', 'd', 'a']
```
Visualizar indices y valores:
```py
lista=['hola',2,5,'jego',10,55,8,4]
for i in range(len(lista)):
    print(f'{i}:{lista[i]}')
```

## Clase 2: Tuplas
Un tupla es un tipo de lista de donde se guardan valores pero **ya no se puede**:
* cambiara valores de los elementos a diferencia de listas.
* Iterar

Se declaran en **paréntesis**()
ejemplo:
```py
# Ejercicio 1: Crear una tupla
tupla=()
print(len(tupla))

# Ejercicio 2: Crear una tupla con elementos
tupla2=('hola','como','estas')
print(len(tupla2))
```
Para llamar un elemento de un tupla, se pone el nombre de la tupla y entre corchetes la posición
```py
# Ejercicio 3: Llamar elementos de una tupla
print(tupla2[1],'se llama para decirle ',tupla2[0])
```

### Listas dentro de una Tupla
```py
# Ejercicio 4: Listas dentro de una tupla y asignar variables a sus elementos
datos_Paciente=('Paolo',[27,54])
nombre , edad_peso = datos_Paciente;

print(nombre)
print(edad_peso)

estatura, peso , temperatura =(1.5,64,20)
print(f'{estatura}-{peso}-{temperatura}')

#Paolo
#[27, 54]
#1.5-64-20
```

### Tuplas dentro de una listas
Enumerar elementos (indices)
```py
nombres=('Paolo','Marlon','Mario')
lista_nombres=list(enumerate(nombres))
tupla_nombres=tuple(enumerate(nombres))

print(lista_nombres)
print(tupla_nombres)

for indice,valor in enumerate(nombres):
    print(f'{indice}:{valor}')


#[(0, 'Paolo'), (1, 'Marlon'), (2, 'Mario')]
#((0, 'Paolo'), (1, 'Marlon'), (2, 'Mario'))

# 0:Paolo
# 1:Marlon
# 2:Mario
```
## Clase 3 : Separando secuencias (Listas)

Extraer elementos de una lista
```py
potencias2=[2,4,8,16,32,64,128,264]
print(potencias2[3:5])
print(potencias2[:5])
print(potencias2[3:])
print(potencias2[:])
print(potencias2[::2])
print(potencias2[::-3])
```


Cambiar elementos de una lista
```py
potencias2[0:3]=['dos','cuatro','ocho']
print(potencias2[:])
print(id(potencias2))
```

Poner valores vacios en la lista
```py
potencias2[0:2]=[]
print(potencias2)
```

Obtener un IDENTIFICADOR de la lista
```py
id(potencias2)
print(id(potencias2))
```

Borrar elementos de una lista (Del)


```py
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
```

## Clase 4: Ordenando Listas y tuplas
Tanto listas y tuplas se ordenan con los comandos:
* `sort()` -> ordena ascendente una lista o tupla
* `sort(reverse = True)` -> ordena descendente una lista o tupla
* `sorted(nombre_de_lista)` -> ordena ascendente una lista o tupla y los asigna a otra lista o tupla.


```py
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


# [15, 15, 18, 20, 24, 26, 89]
# [89, 26, 24, 20, 18, 15, 15]
# [15, 15, 18, 20, 24, 26, 89]
```

### Búsqueda de datos en una lista
```py
#Ejercicio 6: verificar si un elemento está en lista
print(78 in edad3)
```
### Otras funciones para extraer elementos de un lista o tupla
* `lista.insert(index,'elemento')`
* `lista.append('elemento')`
* `lista.extend(listaParaAgregar)`
* `lista.remove()`

```py
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

```
### Contar elementos que se repiten en una lista
```py
#Ejercicio 12: Contar elementos que se repoten en una lista
edades = [15, 21, 16, 19, 20, 16, 19, 15, 21, 17, 18]
print(edades.count(16))

for edad4 in range (15,25):
    print(f'La edad {edad4} se repite {edades.count(edad4)} veces')

# 2
# La edad 15 se repite 2 veces
# La edad 16 se repite 2 veces
# La edad 17 se repite 1 veces
# La edad 18 se repite 1 veces
# La edad 19 se repite 2 veces
# La edad 20 se repite 1 veces
# La edad 21 se repite 2 veces
# La edad 22 se repite 0 veces
# La edad 23 se repite 0 veces
# La edad 24 se repite 0 veces

```
