#numero = input("0 a 9999: ")
#print("Unidade: ", numero[3::])
#print("Dezena: ", numero[2:3:] )
#print("Centena: ", numero[1:2:])
#print("Milher: ", numero[0:1:])

num = int(input("numero: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Unidade:{u}")
print(f"Dezena:{d}")
print(f"Centena:{c}")
print(f"Milher:{m}")

