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




