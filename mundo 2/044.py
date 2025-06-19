prec = float(input("PRECO: "))
print("|FORMAS DE PAGAMENTO|\n 1: A VISTA DINHEIRO/CHEQUE\n 2: A VISTA NO CARTAO\n 3: EM ATE 2X NO CARTAO\n 4: EM 3X OU MAIS NO CARTAO")
a1 = int(input("DIGITE: "))
if a1 == 1:
    desc = prec-((prec*10)/100)
    print("VALOR R${:.2f}".format(desc))
elif a1 == 2:
    desc = prec-((prec*5)/100)
    print("VALOR R${:.2f}".format(desc))
elif a1 == 3:
    print(f"VALOR R${prec:.2f}")
elif a1 == 4:
    desc = prec+((prec*20)/100)
    print("VALOR R${:.2f}".format(desc))
else: 
    print("OPCAO INVALIDA")


