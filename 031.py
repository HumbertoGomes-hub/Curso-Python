print("CALCULADOR DE VIAGEM")
dist = float(input("DISTANCIA EM KM: "))
if dist <= 200:
    prec = dist*0.50
    print("PRECO DA VIAGEM R${:.2f}".format(prec))
else:
    prec = dist*0.45
    print("PRECO DA VIAGEM R${:.2f}".format(prec))
    

#prec = dist * 0.50 if dist <= 200 else dist * 0.45