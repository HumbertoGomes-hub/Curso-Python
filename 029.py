print("RADAR")
vel = int(input("KM/H:"))
lim = 80
if vel > lim:
    print("VOCE EXCEDEU O LIMITE")
    exced = vel - lim
    multa = exced*7
    print("MULTADO NO VALOR DE R${:.2f}".format(multa))
else:
    print("VOCE ESTA NO LIMETE")