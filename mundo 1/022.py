print("|-------------|")
print("|NOME COMPLETO|")
nome = input() 
print("|-------------|")
print("|  MINUSCULAS |")
print(nome.lower())
print("|-------------|")
print("|  MAIUSCULAS |")
print(nome.upper())
print("|-------------|")
print("|  QUANTIDADE |")
print(len(nome.replace(" ", "")))
print("|-------------|")
print("|QUANTIDADE N1|")
lista = nome.split()
print(lista[0],":",len(lista[0]))





nome = str(input("Digite seu nome completo: ")).strip()
print('Analisandg seu nome...')
print( "Seu nome em maiusculo {}".format(nome.upper()))
print("Seu none en minusculo é {}".format(nome. lower()))
print("Seu nome tem ao todo {} letras".format(len(nome)-nome.count(" ")))
#print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
separa = nome.split()
print("Seu primeiro nome e {} e ele tem {} letras".format(separa[0], len(separa[0])))




