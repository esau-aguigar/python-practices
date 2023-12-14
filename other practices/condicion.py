valor = input("Imgresa un entero:")
if valor.isdigit():
    valor = int(valor)

    if valor % 2 == 1:
        print("El entero",valor,"es impar")
    elif valor % 2 == 0:
        print("El entero",valor,"es par")
else:
    print("no puedes ingresar letras!")
