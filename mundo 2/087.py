
matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = 0
max2 = list()
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f"DIGITE UM VALOR [{l,c}]: "))
        if matriz[l][c]%2 == 0:
            par = par + matriz[l][c] 
         
            


for l in range(0,3):
    for c in range (0,3):
        print(f"[{matriz[l][c]:^5}]",end="")
    print()
    
soma3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
max2 =  matriz[1].copy()

print("-="*27)
print(f"SOMA DOS NUMEROS PARES {par}")
print("-="*27)
print(f"SOMA DOS NUMEROS DA TERCEIRA COLUNA {soma3}")
print("-="*27)
print(f"MAIOR VALOR DA SEGUNDA LINHA {max(max2)}")
