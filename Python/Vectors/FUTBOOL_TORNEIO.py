import itertools
import os
os.system("cls")

quantidade_times = int(input("Quantos times deseja colocar no torneio? "))
times = []

for i in range(1, quantidade_times + 1):
    time = input(f"Digite o nome do {i}\u00BA time: ")
    times.append(time)
    
largura_maxima = max(len(time) for time in times)

partidas = list(itertools.permutations(times, 2))

os.system("cls")
print("Tabela de Partidas:")
for partida in partidas:
    time1, time2 = partida
    espacos = " " * (largura_maxima - len(time1))
    print(f"{time1} {espacos}[ ] x [ ] {time2}")