import time
from datetime import date
cad = dict()
nome1 = str(input("NOME: ")).capitalize().strip()
nasc1 = int(input("ANO NASCIMENTO: "))
ctps1 = int(input("NUMERO DA CARTEIRA DE TRABALHO (0 NÃO TEM): "))
ano = date.today().year
idade = ano - nasc1
apo = 0
if ctps1 != 0:
    cad["nome"] = nome1
    cad["ano_contrat"] = int(input("ANO DA CONTRATAÇÃO: "))
    cad["salario"] = float(input("SALÁRIO: "))
    cad["idade"] = idade
    cad["ctps"] = ctps1
    apo = 65 - cad["idade"]
    cad["idade_apo"] = apo + idade
    print(cad)
    print("-="*27)
    print(f"Nome: {cad['nome']} | Idade: {cad['idade']}")
    print("-"*27)
    print(f"Numero ctps: {cad['ctps']} | Idade da aposentadoria: {cad['idade_apo']}")
    print("-"*27)
    print(f"Salario: {cad['salario']} | Ano contratação: {cad['ano_contrat']}")
else:   
    print("NUMERO CTPS INVALIDO!")
    

    
    

    
    
    


