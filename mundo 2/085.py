lmae = list()
par = list()
impar = list()
for c in range (0,7):
    lmae.append(int(input("DIGITE UM VALOR: ")))
    for p in lmae:
        if p%2 == 0:
            par.append(lmae[:])
        else:
            impar.append(lmae[:])
    lmae.clear()
par.sort()
impar.sort()
            
print(f"PAR {par}, IMPAR {impar}")
        