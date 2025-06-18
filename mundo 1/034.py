sal = float(input("SALARIO: "))
if sal >= 1250.00:
    aum = (10*sal)/100
    sal2 = sal + aum
    print(f"novo salario de {sal2:.2f}")
else:
    aum = (15*sal)/100
    sal2 = sal + aum
    print(f"novo salario de {sal2:.2f}")
