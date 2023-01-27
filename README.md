# Curso de Python para data Scientist
## Clase 1: Sentencia if
```py
nac=1999
if 2021-nac>=25:
    print("posible cliente")
```
## Clase 2: Listas y tuplas
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

