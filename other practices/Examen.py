import random

opcion = 0
num = 0
lista=list()
listaCreada = 0
nSiExiste=0
valorValido =0

while opcion != 3:
    opcion = input("MENU \n1-Crear lista \n2-Buscar \n3-Salir \n")

    if opcion.isdigit():
        opcion = int(opcion)
        if opcion<4 and opcion>0:
            if opcion == 1:
                if listaCreada == 1:
                    print("La lista ya fue creada! ")
                else:
                    listaCreada = 1
                    lista.append(random.sample(range(101),1000))
                    print (lista)

            elif opcion == 2:
                while valorValido == 0:
                    num = input("Ingresa un numero:")
                    if num.isdigit():
                        num = int(num)

                        if num<101 and num>0:
                            valorValido = 1
                            for i in range (0,999):
                                if num == lista[i]:
                                    print ("aqui esta",i)
                                    nSiExiste = 1
                            '''-------Fin FOR------------'''
                            if nSiExiste == 0:
                                print ("no se encontro ",n)
                        else:
                            print ("Error! Valor invalido intentalo de nuevo")
                    else:
                        print ("Error! Valor invalido intentalo de nuevo")
                '''------------------Fin del ciclo while-----------------'''
        else:
            print ("Error! Opcion invalida")

    else:
        print ("Error! Opcion invalida")
