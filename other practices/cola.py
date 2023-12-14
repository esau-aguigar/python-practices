class cola:
    def __init__(self):
        self.c = []

    def encolar(self,dato):
        self.c.append(dato)
    def desencolar(self):
        if len(self.c)==0:
            print ("Lista vacia!! No puede desencolar")
        else:
            del self.c[0]
    def cabeza(self):
        if len(self.c)==0:
            print ("Lista vacia!")
        else:
            return self.c[0]
    
    def cla(self):
        if len(self.c)== 0:
            print ("Lista vacia!")
        else:
            return self.c[-1]
    
    def mostrar(self):
        if len(self.c)== 0:
            print ("Lista vacia!")
        else:
             return self.c

colaa=cola()

opc = 1
while opc != 6:
    print("Menu")
    print("1-Mostrar todos")
    print("2-Encolar")
    print("3-Desencolar")
    print("4-Mostrar Primero")
    print("5-Mostrar Ultimo")
    print("6-Salir")
    opc = input()
    if opc.isdigit():
        opc = int(opc)
        if opc <1 and opc <7:
            print("Error Opcion Invalida")
        elif opc == 1:
            print (colaa.mostrar())
        elif opc == 2:
            d = input("ingresa un numero:")
            colaa.encolar(d)
        elif opc == 3:
            colaa.desencolar()
        elif opc == 4:
            print ("Primero ---->",colaa.cabeza())
        elif opc == 5:
            print("Ultimo ---->",colaa.cla())
        elif opc == 6:
            colaa.desencolar()
        else:
            print("Error Opcion Invalida")
    else:
        print("Error Opcion Invalida")
