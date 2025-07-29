from random import randint
quant = int(input("QUANTIADE DE JOGOS: "))
jogo = list()




for c in range(quant):
    cart = list()
    jogo.append(cart) 
    for r in range(0,6):
        a = randint(1,60)
        
        
        if a not in cart:
            cart.append(a)
        else:
            while a in cart:
               a = randint(1,60)
            cart.append(a)    
                
            
          
print(jogo)
print("-="*27)
for c2 in range(quant):
    print(f"CAERTELA {c2+1} : {jogo[c2]}")
           

                
        

    