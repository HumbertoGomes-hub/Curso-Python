print("CALCULADOR DE NOTAS")
n1 = float(input("NOTA 1: "))
n2 = float(input("NORA 2: "))
m = (n1 + n2)/2
if m < 5.0:
    print("ALUNO REPROVADO MEDIA {:.1f}".format(m))
elif m >= 5.0 and m <= 6.9:
    print(f"RECUPERCAO MEDIA {m:.1f}")
else:
    print("ALUNO APROVADO MEDIA {:.1f}".format(m))