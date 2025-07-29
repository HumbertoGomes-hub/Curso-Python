from copy import deepcopy
lista_alunos = list()
aluno = list()
notas_aluno = list()
media = list()
cont = 0
while True:
    aluno.append(str(input("NOME: ")).capitalize().strip())
    nota1 = float(input("NOTA 1: "))
    nota2 = float(input("NOTA 2: "))
    media = [(nota1 + nota2)/2]
    notas_aluno = [nota1,nota2]
    aluno.append(deepcopy(notas_aluno))
    aluno.append(deepcopy(media)) 
    lista_alunos.append(deepcopy(aluno))
    aluno.clear()
    notas_aluno.clear()
    media.clear()
    controle = str(input("QUER CONTINUAR [S/N]: ")).upper().strip()
    cont +=1
    if controle[0] == "N":
        break
    
    
for i,c in enumerate(range(cont)):
    print("-="*30)
    print(f"NUMERO: {i}  ALUNO: {lista_alunos[c][0]}   MEDIA: {lista_alunos[c][2][0]}")
    print("-="*30)

while True:
    num = int(input("NUMERO DO ALUNO QUE DESEJA VER AS NOTAS: "))
    print(f"ALUNO: {lista_alunos[num][0]} NOTA 1: {lista_alunos[num][1][0]} NOTA 2: {lista_alunos[num][1][1]}")
    
    
    controle2 = str(input("QUER CONTINUAR [S/N]: ")).upper().strip()
    cont +=1
    if controle2[0] == "N":
        break  
    
    