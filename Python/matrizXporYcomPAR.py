import os
os.system("cls")

matriz = []

primeiros_numeros = []
for _ in range(3):
    numero = int(input("Digite X números para a matriz: "))
    primeiros_numeros.append(numero)

for _ in range(len(matriz)):
    matriz[_] = primeiros_numeros[:]

os.system("cls")
linhas = int(input("Quantas linhas adicionais você deseja adicionar? "))
colunas = int(input("Quantas colunas adicionais você deseja adicionar? "))

for _ in range(linhas):
    nova_linha = primeiros_numeros[:]
    matriz.append(nova_linha)

for linha in matriz:
    linha.extend([0] * colunas)

print()
print("Matriz preenchida:")
for linha in matriz:
    print(linha)

print()
print("Números pares dentro da matriz:")
for linha in matriz:
    for elemento in linha:
        if elemento % 2 == 0 and elemento != 0:
            print(elemento)
