from random import randint
#import random
pc = randint(1,5)
print("ADIVINHE O NUMERO")
a1 = int(input(""))
if a1 == pc:
    print("VOCE ACERTOU \nPARABENS")
else:
    print("VOCE ERROU \nTENTE NOVAMENTE")



#print("ACERTOU" if pc == a1 else "ERROU") //condicao simplificada
