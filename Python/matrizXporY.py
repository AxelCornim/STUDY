import os
os.system("cls")

matriz = []

linhas = int(input("Qualtas linhas você deseja adicionar na matriz? "))
colunas = int(input("Qualtas colunas você deseja adicionar na matriz? "))

for i in range(linhas):
    nova_linha = [0] * colunas
    matriz.append(nova_linha)
    
print()
print("Matriz preenchida:")
for linha in matriz:
    print(linha)