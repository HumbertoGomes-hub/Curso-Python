import datetime
nasc = int(input("ANO DE NASCIMENTO: "))
ano = datetime.date.today().year
alist = ano - nasc
if alist == 18:
    print("JA ESTA NO ANO DE SE ALISTAR")
elif alist < 18:
    print("FALTAM {} ANOS PARA SE ALISTAR".format(18 - alist))
else:
    print("SE PASSARAM {} ANOS DO SEU ANO DE ALISTAMENTO".format(alist - 18))

