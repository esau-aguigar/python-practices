import time
import random
inicio=time.time()
TAM=100000
lista = []
i=1
j=0
for i in range(TAM):
    lista.append(random.randint(1,100))

for j in range (TAM - 1):
    if lista[j] > lista[j+1]:
        temp = lista[j];
        lista[j] = lista[j+1];
        lista[j+1] = temp;

print("tiempo de:",time.time()-inicio,":segundos")
