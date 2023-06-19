import os
os.system("cls")

quantidade_pessoas = int(input("Quantas pessoas você deseja verificar? "))
nomes_c = []

for i in range(1, quantidade_pessoas + 1):
    nome = input(f"Digite o nome da {i}ª pessoa: ")
    if nome.lower().startswith('c'):
        nomes_c.append(nome)

os.system("cls")
print("Listagem de nomes com 'C':")
for i, nome in enumerate(nomes_c, 1):
    print(f"{i}. {nome}")