import random
print("ADIVINHE O NUMERO")
pc = random.randint(1,5)
n = int(input("DIGITE: "))
tent = 1
while n != pc:
    print("ERROU")
    n = int(input("TENTE NOVAMENTE: "))
    tent +=1
print("GANHOU")
print("VOCE TENTOU {}".format(tent))