import time
from datetime import date
cad = dict()
nome1 = str(input("NOME: ")).capitalize().strip()
nasc1 = int(input("ANO NASCIMENTO: "))
ctps1 = int(input("NUMERO DA CARTEIRA DE TRABALHO (0 NÃO TEM): "))
ano = date.today().year
idade = ano - nasc1
if ctps1 != 0:
    cad["nome"] = nome1
    cad["ano_contrat"] = int(input("ANO DA CONTRATAÇÃO: "))
    cad["salario"] = float(input("SALÁRIO: "))
    cad["idade"] = ano
    
print(cad)  
    
    
    


