def obter_vetor_origem(N1):
    return [N1, N1 + 1, N1 + 2]

def processar_vetor(vetor_origem):
    resultado = [valor * 2 for valor in vetor_origem]
    return resultado

def meu_texto():
    print("____CONTAS DE ELEMENTOS E VETORES____")

meu_texto()
N1 = int(input("-Digite número origem: "))

vetor_origem = obter_vetor_origem(N1)

print("Elemento na posição 0:", vetor_origem[0])
print("Elemento na posição 1:", vetor_origem[1])
print("Elemento na posição 2:", vetor_origem[2])

vetor_origem[2] = vetor_origem[2] + 1
vetor_origem.insert(0, 10)
vetor_origem.insert(1, 15)

subvetor = vetor_origem[0:2]
subvetor2 = vetor_origem[2:3]
subvetor[1] += 5
subvetor.append(25)
subvetor2.append(30)
vetor_oren = subvetor + subvetor2
vetor_oren2 = sorted(vetor_oren) 

print("Valor dos subvetores é:", vetor_oren2)
print("Todos os elementos do vetor original após modificações:", vetor_origem)
print("Elemento na posição 2 após modificação:", vetor_origem[4])
print("O novo valor do vetor 0 após modificação:", vetor_origem[0])

soma = 0
for elemento in vetor_origem:
    soma += elemento
print("Soma de todos os elementos:", soma)

media = soma / len(vetor_origem)
print("Média dos elementos:", media)

dobro = [valor * 2 for valor in vetor_origem]
print("Os elementos dobrados:", dobro)

vetor_ordenado = sorted(vetor_origem)
print("Vetor ordenado em ordem crescente:", vetor_ordenado)

vetor_ordenado = sorted(vetor_origem, reverse=True)
print("Vetor ordenado em ordem decrescente:", vetor_ordenado)
