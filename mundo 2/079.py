lista = list()
while True:
    a = int(input("DIGITE UM VALOR: "))
    while a not in lista:
        lista.append(a)
    cont = str(input("QUER CONTINUAR S/N: ")).upper().strip()
    if cont[0] == "N" :
        break
lista.sort()
print(lista)
    
    
