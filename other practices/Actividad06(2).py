import os

def limpiar():
    os.system("pause")
    os.system("cls")



class Grafo():

    def __init__(self,tipo):
        self.grafo={}
        self.tipo=tipo
        pass

    def agregar_arista(self,origen,destino,peso):
        if origen not in self.grafo:
            self.grafo.update({origen:[]})
        if destino not in self.grafo:
            self.grafo.update({destino:[]})
        if self.tipo == 1:
            if destino not in self.grafo[origen]:
                self.grafo[origen].append(destino)
            if origen not in self.grafo[destino]:
                self.grafo[destino].append(origen)
        else:
            listOri=[destino,peso]
            if listOri not in self.grafo[origen]:
                self.grafo[origen].append(listOri)
                if self.tipo == 2:
                    listDes=[origen,peso]
                    if listDes not in self.grafo[destino]:
                        self.grafo[destino].append(listDes)
        pass

    def mostrar_grafo(self):
        for key, value in self.grafo.items():
            print(key, value)
        pass

    def mostrar_aristas(self,vertice):
        if vertice in self.grafo:
            print (vertice,end=":")
            lista= self.grafo[vertice]
            print (lista)
        pass

    def eliminar_arista(self,origen,destino):
        if self.tipo == 1:
            if origen in self.grafo and destino in self.grafo:
                if destino in self.grafo[origen] and origen in self.grafo[destino]:
                    self.grafo[origen].remove(destino)
                    self.grafo[destino].remove(origen)
        else:
            if origen in self.grafo and destino in self.grafo:
              	for i in self.grafo[origen]:
                    if i[0] == destino:
                        self.grafo[origen].remove(i)
                        if self.tipo == 2:
                            for j in self.grafo[destino]:
                            	if j[0] in origen:
                            		self.grafo[destino].remove(j)
        pass

    def modificar_arista(self,origen,destino):
        bol=0
        if self.tipo == 1:
            if origen in self.grafo and destino in self.grafo:
                if destino in self.grafo[origen] and origen in self.grafo[destino]:
                    self.grafo[origen].remove(destino)
                    self.grafo[destino].remove(origen)
                    bol=1
        else:
            if origen in self.grafo and destino in self.grafo:
                for i in self.grafo[origen]:
                    if i[0] == destino:
                        self.grafo[origen].remove(i)
                        bol=1
                        if self.tipo == 2:
                            for j in self.grafo[destino]:
                                if j[0] in origen:
                                    self.grafo[destino].remove(j)
        pon=0
        if bol == 1:
            print("\nDatos de la nueva arista")
            ori=input("Origen:")
            des=input("Destino:")
            if self.tipo !=1:
                pon=int(input("Ponderacion:"))
            self.agregar_arista(ori,des,pon)

        pass

    def profundidad(self,iniver):
        self.mostrar_grafo()
        visi = []
        cola = []
        impri = []
        cola.append(iniver)
        visi.append(iniver)
        if iniver in self.grafo:
            while cola:
                pos = cola[0]
                print ("Cola    : ",cola)
                impri.append(pos)
                cola.pop(0)
                for key in self.grafo[pos]:
                    if key not in visi:
                        visi.append(key)
                        cola.append(key)
            print ("Que hice. . . \n")
            print ("Visitados   : ",visi)
            print ("Impresiones : ",impri)
        else:
            print ("No existe")
            os.system("pause")
        pass

    def anchura(self,iniver):
        self.mostrar_grafo()
        visi = []
        pila = []
        impri = []
        pila.append(iniver)
        visi.append(iniver)
        if iniver in self.grafo:
            while pila:
                pos = pila[-1]
                print ("Pila     : ",pila)
                impri.append(pos)
                pila.remove(pila[-1])
                for key in self.grafo[pos]:
                    if key not in visi:
                        visi.append(key)
                        pila.append(key)
            print ("Que hice . . . \n")
            print ("Visitados   : ",visi)
            print ("Impresiones : ",impri)
        else:
            print ("No existe")
            os.system("pause")
        pass

    def primm(self,origen,destino,peso):
        pass

    def kruskal(self,origen,destino,peso):
        pass


class menu():
    def __init__(self):
        i=0
        while i==0:
            op = 1
            limpiar()
            grfo=input("MENU \
                            \n1-No dirig.-No ponderado\
                            \n2-No dirig.-Ponderado\
                            \n3-Dirigido-Ponderado\
                            \n0-Salir\
                            \nOpcion:")
            if grfo.isdigit():
	            grfo=int(grfo)	
	            if(grfo>0 and grfo<4):
	            	self.grafo=Grafo(tipo=grfo)
	            elif grfo==0:
	                i=1
	                op=0
	            else:
	            	print("Error: Opcion Invalida")
	            while op!=0:
	                limpiar()
	                pon=0
	                op=int(input("MENU  \n1-Agregar Arista \
			                            \n2-Mostrar Grafo \
			                            \n3-Mostrar Aristas \
			                            \n4-Eliminar Arista \
			                            \n5-Modificar Arista \
			                            \n*6-Recorridos Profundidad \
			                            \n*7-Recorrido Anchura \
			                            \n*8-Primm \
			                            \n*9-Kruskal \
			                            \n0-Volver \
			                            \nOpcion:"))
	                if op==1:
	                    ori=input("Origen:")
	                    des=input("Destino:")
	                    if self.grafo.tipo!=1:
	                    	pon=int(input("Ponderacion:"))
	                    self.grafo.agregar_arista(ori,des,pon)
	                    pass
	                elif op==2:
	                	self.grafo.mostrar_grafo()
	                	pass
	                elif op==3:
	                	vertice=input("Ingrese un vertice:")
	                	self.grafo.mostrar_aristas(vertice)
	                	pass
	                elif op==4:
	                	ori=input("Origen:")
	                	des=input("Destino:")
	                	self.grafo.eliminar_arista(ori,des)
	                	pass
	                elif op==5:
	                    print("Que arista desea modificar")
	                    self.grafo.mostrar_grafo()
	                    ori=input("Origen:")
	                    des=input("Destino:")
	                    self.grafo.modificar_arista(ori,des)
	                    pass
	                elif op==6:
	                    vertice=input("Comenzar en:")
	                    self.grafo.profundidad(vertice)
	                    pass
	                elif op==7:
	                    vertice=input("Comenzar en:")
	                    self.grafo.anchura(vertice)
	                    pass
	                elif op==8:
	                	pass
	                elif op==9:
	                	pass

menu()
