
lista = []
for c in range (5):
    n = int(input("DIGITE UM VALOR: "))
    if c== 0 or n> lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos +=1
print(lista)
        
    

