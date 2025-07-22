print("CADASTRO")
maior = 0
homi = 0
muie = 0
while True:
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO F/M: ")).upper().strip()
    if idade >= 18:
        maior +=1
    if sexo == "M":
        homi += 1
    if sexo == "F" and idade <= 20:
        muie +=1
    cont = str(input("QUER CONTINUAR S/N: ")).upper().strip()
    if cont == "N":
        break
print(f"MAIORES DE 18: {maior}, HOMEMS: {homi}, MULHERES MENORES DE 20: {muie}")
