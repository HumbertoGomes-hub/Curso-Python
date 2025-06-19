r1 = float(input("reta "))
r2 = float(input("reta "))
r3 = float(input("reta "))
if (r1 + r2) > r3 and (r2 + r3) > r1 and (r1 + r3) > r2:
    if r1 == r2 == r3:
        print("EQUILATERO")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("ISOSCELES")
    elif r1 != r2 != r3:
        print("ESCALENO")
else:
    print("VALORES INVALIDOS")