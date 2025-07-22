print("TABUADA")
while True:
    tabu = int(input("DIGITE: "))
    c = 0
    for c in range (1,11):
        res = tabu * c
        print(f"{tabu} x {c}=", res)
        c += 1
    if tabu== 999:
        break