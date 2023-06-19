# Vetor de elementos
vetor = [10, 20, 30, 40, 50]

# Acesso de elementos usando índice
print("Elemento na posição 0:", vetor[0])
print("Elemento na posição 2:", vetor[2])
print("Elemento na posição 4:", vetor[4])
print()

# Modificando valor do segundo elemento
vetor[1] = 25

# Vetor percorrido pelo loop para acessar os elementos
print("Elementos do vetor:")
print()
for i in range(len(vetor)):
    print("Elemento na posição", i, ":", vetor[i])