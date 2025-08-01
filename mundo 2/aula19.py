pessoas = {"nome": "Humberto", "sexo": "M", "idade": 18}
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")

del pessoas ["sexo"]
pessoas["idade"] = 19
pessoas["peso"] = 67.5

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print("-="*27)

for k in pessoas.keys():
    print(k)
print("-="*27)
for k in pessoas.values():
    print(k)
print("-="*27)
for k,v in pessoas.items():
    print(f"{k}={v}")
 
brasil = list()
estado1 = {"uf":"São Paulo", "sigla":"SP"}
estado2 = {"uf":"Rio de Janeiro","sigla":"RJ"}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]["uf"])

