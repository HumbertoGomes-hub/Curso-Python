n1 = float(input("NOTA: "))
n2 = float(input("NOTA: "))
med = (n1 + n2)/2
print("MEDIA {:.2f}".format(med))
print("APROVADO" if med >= 6.0 else "REPROVADO")
