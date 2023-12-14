import datetime

year = input("Ingresa tu AÑO de nacimiento:")
if year.isdigit():
    year = int(year)
    mes = input("Ingresa tu MES de nacimiento:")
    if mes.isdigit():
        mes = int(mes)
        dia = input("Ingresa tu DIA de nacimiento:")
        if dia.isdigit():
            dia = int(dia)

            print ("\n")

            try:
                fecha = datetime.date(year,mes,dia)
                print ("Tu signo es:")
                if mes == 3 and dia>=21 or mes == 4 and dia<=21:
                    print ("aries")
                elif mes == 4 and dia>=22 or mes == 5 and dia<=21:
                    print ("Tauro")
                elif mes == 5 and dia>=22 or mes == 6 and dia<=21:
                    print ("Geminis")
                elif mes == 6 and dia>=22 or mes == 7 and dia<=21:
                    print ("Cancer")
                elif mes == 7 and dia>=22 or mes == 8 and dia<=21:
                    print ("Leo")
                elif mes == 8 and dia>=22 or mes == 9 and dia<=21:
                    print ("Virgo")
                elif mes == 9 and dia>=22 or mes == 10 and dia<=21:
                    print ("Libra")
                elif mes == 10 and dia>=22 or mes == 11 and dia<=21:
                    print ("Escorpio")
                elif mes == 11 and dia>=22 or mes == 12 and dia<=21:
                    print ("Sagitario")
                elif mes == 12 and dia>=22 or mes == 1 and dia<=21:
                    print ("Capricornio")
                elif mes == 1 and dia>=22 or mes == 2 and dia<=21:
                    print ("Acuario")
                elif mes == 2 and dia>=22 or mes == 3 and dia<=21:
                    print ("Picis")

                print("y naciste un")

                if fecha.weekday() == 0:
                    print ("Lunes")
                elif fecha.weekday() == 1:
                    print ("Martes")
                elif fecha.weekday() == 2:
                    print ("Miercoles")
                elif fecha.weekday() == 3:
                    print ("Jueves")
                elif fecha.weekday() == 4:
                    print ("Viernes")
                elif fecha.weekday() == 5:
                    print ("Sabado")
                elif fecha.weekday() == 6:
                    print ("Domingo")

            except ValueError:
                print("Hubo un error en la fecha")
        else:
            print("Error! no se permiten letras")
    else:
        print("Error! no se permiten letras")
else:
    print("Error! no se permiten letras")
