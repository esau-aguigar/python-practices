class pila:
    def __init__(self):
        self.p = []

    def apilar(self,dato):
        self.p.append(dato)
    def desapilar(self):
        if len(self.p)==0:
            print ("Lista vacia!!")
        else:
            del self.p[-1]
    def tope(self):
        return self.p[-1]

Pila=pila()
Pila.apilar(4)
Pila.apilar(1)
Pila.apilar(10)
print (Pila.tope())
Pila.desapilar()
print (Pila.tope())
