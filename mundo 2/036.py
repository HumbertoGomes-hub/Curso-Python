print("|SIMULADOR DE EMPRESTIMO|")
casa = float(input("VALOR DA CASA: "))
sal = float(input("VALOR DO SALARIO: "))
anos = int(input("ANOS DO PARCELAMENTO: "))
parceano = casa/anos
parce = parceano/12
porc = (30*sal)/100
if parce <= porc:
    print(f"O valor da parcela: {parce:.2f}")
else:
    print("EMPRESTIMO NEGADO")
    
