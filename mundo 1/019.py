import random
a1 = input("ALUNO 1 : ")
a2 = input("ALUNO 2 : ")
a3 = input("ALUNO 3 : ")
a4 = input("ALUNO 4 : ")
alunos = [a1,a2,a3,a4]
sort = random.choice(alunos)
print(f"aluno escolhido: {sort}")