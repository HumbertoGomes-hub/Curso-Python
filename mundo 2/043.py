print("CALCULADORA IMC")
altura = float(input("ALTURA: "))
peso = float(input("PESO: "))
i = altura * altura
imc = peso / i 
if imc < 18.5:
    print(f"ABAIXO DO PESO IMC {imc:.2f}")
elif imc >= 18.5 and imc < 25:
    print(f"PESO IDEAL IMC {imc:.2f}")
elif imc >= 25 and imc <= 30:
    print(f"SOBREPESO IMC {imc:.2f}")
elif imc > 30 and imc <= 40:
    print(f"OBESIDADE IMC {imc:.2f}")
else:
    print(f"OBESIDADE MORBIDA IMC {imc:.2f}")