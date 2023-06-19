import random
import os
os.system("cls")

N1 = int(input("Valor de N1: "))
N2 = int(input("Valor de N2: "))

ale_torio = random.randint(N1, N2)

os.system("cls")
print("Número aleatorio de", N1,"até", N2)
print("Random number:", ale_torio)