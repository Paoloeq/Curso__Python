#Ejercicio 1: Conjunto de valores en una lista
##Metodo normal
lista=[]
for dato in range (0,10):
    lista.append(dato)

print(lista)

##Metodo Compresión de listas
lista1=[dato for dato in range (0,10)]
print(lista1)

##Utilizando comando list
lista2=list(range(0,10))
print(lista2)

#Ejercicio 2: Pooner los cubos en una lista usando "Comprension de lista"
cua2=[num**3 for num in range (0,10)]
print(cua2)
print(id(cua2))

#Ejercicio 3: Poner condicionales 
cua2=[num**2 for num in range (0,10) if num**2<50]
print(cua2)
