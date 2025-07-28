lmae = list()
par = list()
impar = list()
a = 0
for c in range (0,7):
    a = int(input("DIGITE UM VALOR: "))
    if a%2 == 0:
        par.append(a)
    else:
        impar.append(a)
impar.sort()
par.sort()
lmae.append(impar[:])
lmae.append(par[:])
print(f"VALORES IMPARES: {lmae[0]}, VALORES PARES: {lmae[1]}")
        