tope = input("Ingresa un numero:")
tope = int(tope)
n = 1
sumatoria=0
while n<=5:
    print ("esto vale n=", n)
    factorial=n-1
    d=n
    print ("esto vale factorial=", factorial)

    while factorial>0:
        d=(d*factorial)
        factorial-=1
    print ("----------factorial de",n,"=>",d)
    sumatoria=sumatoria+(1/d)
    print ("esto vale sumatoria=", sumatoria)

    n+=1
print("resultado: ",sumatoria)
