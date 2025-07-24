lista = []

for c in range(5):
    lista.append(int(input("Digite um número: ")))

print(f"\nLista digitada: {lista}")
print("-" * 40)

maior = max(lista)
menor = min(lista)

print(f"Maior valor: {maior} nas posições: ", end='')
for i, valor in enumerate(lista):
    if valor == maior:
        print(i, end=' ')

print(f"\nMenor valor: {menor} nas posições: ", end='')
for i, valor in enumerate(lista):
    if valor == menor:
        print(i, end=' ')
