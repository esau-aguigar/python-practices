import zipfile
import string
import time
import os

inicio = time.time()
lista= []
for i in range(26):
    lista.append(string.ascii_uppercase[i])
for i in range(26):
    lista.append(string.ascii_lowercase[i])
for i in range(10):
    num=str(i)
    lista.append(num)

archivo = zipfile.ZipFile("act03.zip")
bol=0
clve=['A','A','A','A','A']
lim=len(lista)
for i in range (lim):
    if bol==1:
        break
    else:
        clve[0]=lista[i+11]
    for j in range (lim):
        if bol==1:
            break
        else:
            clve[1]=lista[j]
        for k in range (lim):
            if bol==1:
                break
            else:
                clve[2]=lista[k]
            for l in range (lim):
                if bol==1:
                    break
                else:
                    clve[3]=lista[l]
                for m in range (lim):
                    if bol==1:
                        break
                    else:
                        clve[4]=lista[m]
                        clave = "".join(clve)
                    try:
                        archivo.extractall(pwd=clave.encode())
                        print("Se ha encontrado la clave:",clave)
                        os.system("pause")
                        bol=1;
                    except Exception as e:
                        print(clave)
print("Tiempo:",time.time()-inicio,"segundos")
