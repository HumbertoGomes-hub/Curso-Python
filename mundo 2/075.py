tupla = (int(input("")),int(input("")),int(input("")),int(input("")),int(input("")))
print(tupla)
print("ddd",tupla.count(9))
if 3 in tupla:
    print("bb",tupla.index(3)+1)
for n in tupla:
    if n % 2 ==0:
        print("aaaaa",n)


