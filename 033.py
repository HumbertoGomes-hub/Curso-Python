n1 = int(input("NUMERO :"))
n2 = int(input("NUMERO :"))
n3 = int(input("NUMERO :"))
if n1 > n2 and n1 > n3 and n2 > n3:
    print(f"MAIOR: {n1} MENOR: {n3}")
elif n2 > n1 and n2 > n3 and n3 > n1:
    print(f"MAIOR: {n2} MENOR: {n1}")
elif n3 > n1 and n3 > n2 and n1 > n2:
    print(f"MAIOR: {n3} MENOR: {n2}")
elif n1 > n2 and n1 > n3 and n2 == n3:
    print(f"MAIOR: {n1} MENOR: {n2}")
elif n2 > n1 and n2 > n3 and n1 == n3:
    print(f"MAIOR: {n2} MENOR: {n1}")
elif n3 > n1 and n3 > n2 and n1 == n2:
    print(f"MAIOR: {n3} MENOR: {n1}")
elif n1 == n2 and n1 > n3 and n2 > n3:
    print(f"MAIOR: {n1} MENOR: {n3}")
elif n2 == n3 and n2 > n1 and n3 > n1:
    print(f"MAIOR: {n2} MENOR: {n1}")
else:
    print("TODOS SAO IGUAIS")



