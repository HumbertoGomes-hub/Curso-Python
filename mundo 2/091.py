from random import randint
dado = dict()
for c in range(1,5):
    lado = randint(1,6)
    dado[f"jogador{c}"] = lado
for k,v in dado.items():
    print(f"O {k} tirou {v}")



    
    