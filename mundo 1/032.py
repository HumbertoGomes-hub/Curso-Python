import datetime
print("VERFICADOR DE ANO BISSEXTO E O PARA O ANO ATUAL")
ano = int(input("ANO : "))
if ano == 0:
    ano = datetime.date.today().year

biss = ano%4
bis = ano%100
bsi1 = ano%400
if biss == 0 and bis != 0 or bsi1 == 0:
    print("E BISSEXTO")
else:
    print("NAO E BISSEXTO")

