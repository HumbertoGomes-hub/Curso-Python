print("CADASTRO")
maior = 0
homi = 0
muie = 0
while True:
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO: ")).upper().strip()
    cont = str(input("QUER CONTINUAR S/N: ")).upper().strip()
    if cont == "S" or cont == "S":
        break
    if idade >= 18:
        maior +=1
print(maior)
