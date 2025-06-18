nome = str(input("DIGITE...")).strip().lower().title()
print(f"\033[0;31;43m{nome}\033[m")
         


core = {"azul":"\033[0;34m", 
        "vermelho":"\033[0;31m"}

print(f"{core['vermelho']}SANTOS")