import os

cadeiras = {}
for i in range(1, 11):
    cadeiras["B" + str(i)] = "C"
    
while True:
    os.system("cls")
    print("Cadeiras disponíveis:")
    for i in range(1, 11):
        cadeira = "B" + str(i)
        status = "[{}]".format(cadeira) if cadeiras[cadeira] == "C" else "[--]"    
        print(status, end=" ")
        
    print()
    cadeira = input("Reservar a cadeira: ").upper()
    if cadeira not in cadeiras:
        print("Cadeira inválida!")
    if cadeiras[cadeira] == "C":
        cadeiras[cadeira] = "[--]"
        print("Cadeira", cadeira, "RESERVADA!")
    else:
        print("Cadeira", cadeira, "já está reservada!")
        
    opcao = input("Quer reservar outra cadeira? [S/N] ").upper()
    if opcao != "S":
        print("Fim Das Escolhas!")
        break