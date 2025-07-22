import random
import time
print("ADIVINHE O NUMERO")
pc = random.randint(1,10)
n = int(input("DIGITE: "))
tent = 1
print(".....")
time.sleep(3)
while n != pc:
    print("ERROU")
    n = int(input("TENTE NOVAMENTE: "))
    print("...")
    time.sleep(3)
    tent +=1
print("GANHOU")
print("VOCE TENTOU {}".format(tent))