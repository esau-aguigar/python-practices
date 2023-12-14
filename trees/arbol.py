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
					sel.insertar(t-right,d)
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
			print (t.dato)
			self.mostrar(t.right)
			
arbol = tree()
arbol.insertar(arbol.root,10)
arbol.insertar(arbol.root,9)
arbol.insertar(arbol.root,8)
arbol.insertar(arbol.root,7)
arbol.mostrar(arbol.root)