lista = []
while True:
    lista.append(int(input("DIGITE UM VALOR: ")))
    trava = str(input("QUER CONTINUAR S/N: ")).upper().strip()
    if trava[0] == "N":
        break
print("-"*30)
print(f"QUANTIDADE DE NUMEROS DIGITADOS: {len(lista)}")
print("-"*30)
lista.sort(reverse=True)
print(f"ORDEM DECRESCENTE: {lista}")
print("-"*30)
if 5 in lista:
    print("NUMERO 5 ESTA PRESENTE NA LISTA")
else:
    print("NUMERO 5 NAO ESTA PRESENTE NA LISTA")

