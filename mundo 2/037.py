print("|CONVERSOR DE BASE|\n |DIGITE \n |1 PARA BINARIA|\n |2 PARA OCTAL|\n |3 PARA HEXADECIMAL|")
num = int(input("DIGITE: "))
val = int(input("NUMERO PARA CONVERTER: "))
if num == 1:
    print("BINARIA: ",bin(val))
elif num == 2:
    print("OCTAL: ", oct(val))
elif num == 3:
    print("HEXADECIMAL: ", hex(val))
else:
    print("ERRO(COMANDO INVALIDO)")
