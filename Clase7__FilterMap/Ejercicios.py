
#lambda
num = ( x for x in range (1,20))

num_pares = list(filter(lambda i: i%2==0,num))
print(num_pares)

#map

multi3 =list(map( lambda m: m*3, num_pares))

print(multi3)