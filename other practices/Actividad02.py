import os


valor=[100,50,20,10,5,1]
op=0
prod=0
pay=0
vuelto=0
while(op!=4):
    os.system("pause")
    os.system("cls")
    print("1-Agua = 8$")
    print("2-Galletas de Nata = 11$")
    print("3-Sandwich Vegetariano = 25$")
    print("4-Salir")
    op=input(" ")
    if op.isdigit():
        op=int(op)
        if op>4:
            print("Error intentelo de nuevo")
        elif op>0 and op<4:
            if op==1: prod=8
            if op==2: prod=11
            if op==3: prod=25
            pay=0

            while pay<prod:
                pay=input("Ingresa Efectivo:")
                if pay.isdigit():
                    pay=int(pay)
                    if pay<prod:
                        print("No te alcanza")
                else:
                    print("Error intentelo de nuevo")
            i=0
            vuelto=pay-prod
            print("Cambio:",vuelto)
            while vuelto!=0:
                if(valor[i]>vuelto):
                    i+=1
                else:
                    vuelto=vuelto-valor[i]
                    print(valor[i])
    else:
        print("Error intentelo de nuevo")
