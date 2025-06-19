import datetime
print("NATACAO")
nasc = int(input("ANO DE NASCIMENTO: "))
atl = datetime.date.today().year
idade = atl - nasc
if idade <= 9:
    print("MIRIM")
elif idade > 9 and idade <= 14:
    print("INFANTIL")
elif idade > 14 and idade <=19:
    print("JUNIOR")
elif idade > 19 and idade <= 20:
    print("SENIOR")
else:
    print("MASTER")