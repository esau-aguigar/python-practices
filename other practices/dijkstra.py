import os
import random

def limpiar():
    os.system("pause")
    os.system("cls")

class Grafo():
    def __init__(self,tipo):
        self.grafo={'GDL':[['MTY',450],['BJX',250],['MZT',500],['MEX',500]],
                    'MTY':[['BJX',700]],
                    'BJX':[['SAN',900],['TAM',400],['MEX',350]],
                    'MZT':[['TIJ',400],['BJX',300]],
                    'TIJ':[['MTY',800]],
                    'TAM':[['MID',450]],
                    'SAN':[['MID',1200]],
                    'MEX':[['MID',450],['CUN',650]],
                    'CUN':[['GDL',650]],
                    'MID':[]}
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

    def Dijkstra(self,actual):
        ori=actual
        print("","Grafo")
        self.mostrar_grafo()
        visit=[]
        aux=[]
        nodos={}
        origenes={}
        lista=[]
        out=1
        for key in self.grafo:
            nodos.update({key:[]})
            nodos[key].append('inf')
            origenes.update({key:[]})
            origenes[key].append('ori')
        nodos[actual][0]=0
        origenes[actual][0]=actual
        visit.append(actual)
        #----------------------------------------
        while len(visit)<len(nodos) and out==1:

            for value in self.grafo[actual]:
                aux.append(actual)
                aux.append(value)
                if aux not in lista:
                    aux[1][1]+=nodos[actual][0]
                    lista.append(aux)
                aux=[]
            for i in range(1,len(lista)):
                j=i
                while j>0 and lista[j][1][1]<lista[j-1][1][1]:
                    lista[j], lista[j-1]=lista[j-1],lista[j]
                    j=j-1
            #print(lista)
            if len(lista)==0:
                print("no puede salir de aqui")
                out=0
            else:
                if nodos[lista[0][1][0]][0]=='inf':
                    nodos[lista[0][1][0]][0]=lista[0][1][1]
                    origenes[lista[0][1][0]][0]=lista[0][0]
                    visit.append(lista[0][1][0])
                    actual=lista[0][1][0]

                elif nodos[lista[0][1][0]][0] > lista[0][1][1]:
                    nodos[lista[0][1][0]][0] = lista[0][1][1]
                    origenes[ lista[0][1][0] ][0]=lista[0][0]
                    visit.append(lista[0][1][0])
                    actual=lista[0][1][0]

                lista.remove(lista[0])
        if out!=0:
            des=input("Ingresa destino:")
            while ori != des:
                print(des,nodos[des][0],"->",origenes[des][0])
                des=origenes[des][0]

        for key in nodos:
            print("nodo:",key,":",nodos[key],"  |  ",key,":",origenes[key])


class menu():
    def __init__(self):
        i=0
        while i==0:
            op = 1
            self.grafo=Grafo(tipo=3)
            i=1
            while op!=0:
                limpiar()
                pon=0
                op=int(input("MENU  \n1-Agregar Arista \
		                            \n2-Mostrar Grafo \
		                            \n3-Mostrar Aristas \
		                            \n4-Eliminar Arista \
		                            \n5-Modificar Arista \
		                            \n6-Dijkstra \
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
                    ori=input("Origen:")
                    self.grafo.Dijkstra(ori)
                    pass
menu()
