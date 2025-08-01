sit = dict()
sit["nome"] = str(input("NOME: ")).capitalize().strip()
sit["media"] = float(input("MEDIA: "))
 
print(f"O aluno(a): {sit['nome']}")
print(f"Tem media: {sit['media']}")
if sit["media"] < 5.0:
    print(f"O aluno(a): {sit['nome']} esta reprovado.")
elif sit["media"] >= 5.0 and sit["media"] <= 6.9:
    print(f"O aluno(a): {sit['nome']} esta de recuperação.")
else:
    print(f"Aluno(a) {sit['nome']} aprovado.")



