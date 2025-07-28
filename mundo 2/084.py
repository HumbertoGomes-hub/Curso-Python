nome = list()
cadastro = list()
maxp = list()
minp = list()
while True:
    nome.append(str(input("MOME: ").capitalize().strip()))
    nome.append(float(input("PESO: ")))
    cadastro.append(nome[:])
    if len(cadastro) == 0:
        maxp = minp = cadastro
    else:
        if cadastro[1] > maxp:
            maxp.append(cadastro[:])
    trava = str(input("QUER CONTINUAR S/N: ").strip().upper())
    if trava[0] == "N":
        break
    nome.clear()
print(f"cadas{cadastro}, max{maxp}")
    
    
    
    
    
    


