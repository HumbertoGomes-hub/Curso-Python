import random
print("|JOKENPO|")
print("---------")
pc = random.randint(1,3)
print("1: PEDRA\n2: PAPEL\n3: TESOURA")
person = int(input("DIGITE: "))
if person >= 1 and person <= 3:
    if person == pc:
        print("EMPATE")
    elif person == 1 and pc == 3:
        print("GANHOU, TESOURA QUEBRA PEDRA")
    elif person == 1 and pc == 2:
        print("PERDEU, PAPEL EMBRULHA PEDRA")
    elif person == 2 and pc == 1:
        print("GANHOU, PAPEL EMBRULHA PEDRA")
    elif person == 3 and pc == 1:
        print("PERDEU, TESOURA QUEBRA PEDRA")
    elif person == 3 and pc == 2:
        print("GANHOU, TESOURA CORTA PAPEL")
    elif person == 2 and pc == 3:
        print("PERDEU, TESOURA CORTA PAPEL")
else:
    print("NUMERO INVALIDO")
    
    