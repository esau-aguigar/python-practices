import random
import time

class nodo():
	def __init__(self,d):
		self.left=None
		self.right=None
		self.dato=d

class tree():
	def __init__(self):
		self.root=None

	def insertar(self,t,d):
		if self.root==None:
			self.root=nodo(d)
		else:
			if d > t.dato:
				if t.right==None:
					t.right=nodo(d)
				else:
					self.insertar(t.right,d)
			else:
				if t.left==None:
					t.left=nodo(d)
				else:
					self.insertar(t.left,d)

	def mostrar(self,t):
		if t==None:
			return None
		else:
			self.mostrar(t.left)
			#print (t.dato, end=",")
			self.mostrar(t.right)
			print (t.dato, end=",")

inicio=time.time()
arbol = tree()
num=1000
for i in range (num):
	arbol.insertar(arbol.root,random.randint(1,100))

arbol.mostrar(arbol.root)
print("\n Tiempo:",time.time()-inicio," segundos")
