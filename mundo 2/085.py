lmae = [[],[]]
a = 0
for c in range (0,7):
    a = int(input("DIGITE UM VALOR: "))
    if a%2 == 0:
        lmae[0].append(a)
    else:
        lmae[1].append(a)
lmae[0].sort()
lmae[1].sort()

print(f"VALORES IMPARES: {lmae[1]}, VALORES PARES: {lmae[0]}")
        