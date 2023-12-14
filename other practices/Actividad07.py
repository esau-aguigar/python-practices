import os
import random

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

    def profundidad(self):
        self.mostrar_grafo()
        nodos=[]
        for key in self.grafo:
        	nodos.append(key)
        ver=random.randint(0,len(nodos)-1)
        iniver=nodos[ver]
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
            print ("Recorrido Profundidad:",impri)
        else:
            print ("No existe")
            os.system("pause")
        pass

    def anchura(self):
        self.mostrar_grafo()
        nodos=[]
        for key in self.grafo:
        	nodos.append(key)
        ver=random.randint(0,len(nodos)-1)
        iniver=nodos[ver]
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
            print ("Recorrido anchura:",impri)
        else:
            print ("No existe")
            os.system("pause")
        pass

    def OrdnIns(slef,lisOrdnada):
        for i in range(1,len(lisOrdnada)):
            j = i
            while j > 0 and lisOrdnada[j][1][1] < lisOrdnada[j-1][1][1]:
                lisOrdnada[j][1][1], lisOrdnada[j-1][1][1] = lisOrdnada[j-1][1][1], lisOrdnada[j][1][1]
                j=j-1

    def primmALG(self):
        print("","Grafo")
        self.mostrar_grafo()
        visit=[]
        nvoGrfo={}
        lisOrdnada=[]
        nodos=[]
        elementos=[]
        for key in self.grafo:
            nodos.append(key)
        print("Nodos:",nodos)
        ver=random.randint(0,len(nodos)-1)
        verIni=nodos[ver]
        print("Origen:",verIni)
        visit.append(verIni)
        for value in self.grafo[verIni]:
            elementos.append(verIni)
            elementos.append(value)
            lisOrdnada.append(elementos)
            elementos=[]
        for i in range(1,len(lisOrdnada)):
            j=i
            while j>0 and lisOrdnada[j][1][1]<lisOrdnada[j-1][1][1]:
                lisOrdnada[j][1], lisOrdnada[j-1][1]=lisOrdnada[j-1][1],lisOrdnada[j][1]
                j=j-1
        if verIni not in nvoGrfo:
            nvoGrfo.update({verIni:[]})
        print("Lista: ",lisOrdnada)
        while len(visit)<len(nodos):
            if verIni not in visit:
                visit.append(verIni)
                for value in self.grafo[verIni]:
                    if value not in lisOrdnada:
                        elementos.append(verIni)
                        elementos.append(value)
                        lisOrdnada.append(elementos)
                        elementos=[]
                for i in range(1,len(lisOrdnada)):
                    j = i
                    while j > 0 and lisOrdnada[j][1][1] < lisOrdnada[j-1][1][1]:
                        lisOrdnada[j], lisOrdnada[j-1] = lisOrdnada[j-1], lisOrdnada[j]
                        j=j-1
                print("Lista: ",lisOrdnada)
            verIni=lisOrdnada[0][1][0]
            if verIni not in nvoGrfo:
                nvoGrfo.update({verIni:[]})
            if lisOrdnada[0][1][0] not in visit:
                nvoGrfo[lisOrdnada[0][0]].append(lisOrdnada[0][1])
            lisOrdnada.remove(lisOrdnada[0])
        for key,value in nvoGrfo.items():
            print(key,value)

    '''def kruskal(self,origen,destino,peso):
    	grafKrus={}
    	lisOrdn=[]
    	lisOrdn=self.grafo.items()

    	#while lisOrdn != NULL:
    	pass
'''

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
			                            \n6-Recorridos Profundidad (solo tipo 1) \
			                            \n7-Recorrido Anchura (solo tipo 1) \
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
	                	if self.grafo.tipo==1:
	                		self.grafo.profundidad()
	                	else:
	                		print("opcion no disponible para este grafo")
	                	pass
	                elif op==7:
	                	if self.grafo.tipo==1:
	                		self.grafo.anchura()
	                	else:
	                		print("opcion no disponible para este grafo")
	                	pass
	                elif op==8:
	                	self.grafo.primmALG()
	                	pass
	                elif op==9:
	                	pass

menu()
