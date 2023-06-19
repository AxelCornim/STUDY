import os
os.system("cls")

vetor_origem = int(input("Quantos elementos deseja adicionar no vetor? "))
vetor = []

for numero in range(1, vetor_origem + 1):
    elemento = int(input(f"Digite o {numero}\u00BA elemento: "))
    vetor.append(elemento)

vetor_ordenado = sorted(vetor)

os.system("cls")
print("Elementos em ordem crescente:")
for elemento in vetor_ordenado:
    print(f"{elemento}", end=" ")