import os 
os.system("cls")

matriz = [[0, 0,], [0, 0], [0, 0], [0, 0]]

for i in range(4):
    for j in range(2):
        valor = int(input(f"Digite o valor para posição [{i}][{j}]: "))
        matriz[i][j] = valor
      
print("MAtriz preenchida:")  
for linha in matriz:
    print(linha)