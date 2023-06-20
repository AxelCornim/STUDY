import os
os.system("cls")

linhas = int(input("Quantas linhas você deseja adicionar? "))
colunas = int(input("Quantas colunas você deseja adicionar? "))

matriz = []

NumMar = int(input("Digite o número Y que deseja colocar na matriz: "))

primeiros_numeros = []
for _ in range(NumMar):
    numero = int(input("Digite X números para a matriz: "))
    primeiros_numeros.append(numero)

for _ in range(linhas):
    linha = []
    for _ in range(colunas):
        linha.append(primeiros_numeros[_ % NumMar])
    matriz.append(linha)

os.system("cls")
print("Matriz preenchida:")
for linha in matriz:
    print(linha)

print()
print("Números pares dentro da matriz:")
for linha in matriz:
    for elemento in linha:
        if elemento % 2 == 0 and elemento != 0:
            print(elemento)