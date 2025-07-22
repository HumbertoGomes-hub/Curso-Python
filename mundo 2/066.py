c = 0
s = 0
while True:
    n = int(input("DIGITE UM NUMERO: "))
    if n == 999:
        break
    s = s + n
    c +=1
print(f"VOCE DIGIOU {c} E A SOMA FOI {s}")