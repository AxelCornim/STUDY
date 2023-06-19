vetor = []

vetor.append(10)
vetor.append(20)
vetor.append(30)
vetor.append(40)
vetor.append(50)

print("A. Elemento na posição 0:", vetor[0])
print("B. Elemento na posição 1:", vetor[2])
print("C. Elemento na posição 2:", vetor[4])

vetor[1] = 25

elemento_removido = vetor.pop(3)

print()
print("Vetor após as autalizações:", vetor)
print("Bloca B removido:", elemento_removido)
print("B. Elemento na posição 1:", vetor[2])