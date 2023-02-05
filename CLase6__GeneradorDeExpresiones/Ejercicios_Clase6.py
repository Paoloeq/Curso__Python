#Generador de Expresiones
lista = [-2,-1,0,1,2,3,4,5,6]
cuadrados_pares=(x**2 for x in lista if x%2==0 )
print(cuadrados_pares)
#<generator object <genexpr> at 0x00000211DC4B42B0>

#Para obtener la lista, hago el llamado
print(list(cuadrados_pares))
#[4, 0, 4, 16, 36]


# Ejemplo de Filter:
numeros =(dato for dato in range(1,20))

def pares(x):
    return x%2==0

numeros_pares = list(filter(pares,numeros))
print(numeros_pares)