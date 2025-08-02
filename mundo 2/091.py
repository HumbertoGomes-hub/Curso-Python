from random import randint
from operator import itemgetter
from time import sleep
dado = dict()
rank = dict()
for c in range(1,5):
    lado = randint(1,6)
    dado[f"jogador{c}"] = lado
for k,v in dado.items():
    print(f"O {k} tirou {v} no dado.")
    sleep(0.4)
rank = sorted(dado.items(), key=itemgetter(1), reverse=True)
print("-="*27)
for i,v in enumerate(rank):
    print(f"O {i+1}° Lugar foi {v[0]} com o lado {v[1]}.")
    sleep(0.4)







    
    