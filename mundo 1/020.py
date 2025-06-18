import random
g1 = input("GRUPO 1: ")
g2 = input("GRUPO 2: ")
g3 = input("GRUPO 3: ")
g4 = input("GRUPO 4: ")
lsit = [g1,g2,g3,g4]
ordem = random.shuffle(lsit)
print(f"A ORDEM E {lsit}")