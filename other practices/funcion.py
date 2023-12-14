def escribir(texto):
    f = open('salida.txt','a')
    f.write(texto)
    f.write('\n')
    f.close()

escribir('Michel Davalos')
