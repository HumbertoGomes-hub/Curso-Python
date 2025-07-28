nome = list()
cadastro = list()
maxp = 0
minp = 0
while True:
    nome.append(str(input("NOME: ").capitalize().strip()))
    nome.append(float(input("PESO: ")))
    if len(cadastro) == 0:
        maxp = minp = nome[1]
    else:
        if nome[1] > maxp:
            maxp = nome[1]
        if nome[1] < minp:
            minp = nome[1]
    cadastro.append(nome[:])
    trava = str(input("QUER CONTINUAR S/N: ").strip().upper())
    if trava[0] == "N":
        break
    nome.clear()
print(f"QUANTIDADE DE PESSOA CADASTRADAS: {len(cadastro)}")
print(f"MAIORES PESOS SÃO {maxp}KG DAS PESSOAS ",end="")
for p in cadastro:
    if p[1] == maxp:
        print(f"[{p[0]}]",end="")
print()
print(f"MENORES PESOS SÃO {minp}KG DAS PESSOAS",end="")
for p in cadastro:
    if p[1] == minp:
        print(f"[{p[0]}]",end="")

    
    
    
    
    
    


