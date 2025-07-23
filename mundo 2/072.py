n = ("zero","um","dois","treis","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezeseis","dezesete","dezoioto","dezenove","vinte")
while True:
    tcl = int(input("DIGITE UM NUMERO ENTRE 0 E 20: "))
    if 0 <= tcl <= 20:
        print((n[tcl]).upper())
        break
    print("TENTE NOVAMENTE")