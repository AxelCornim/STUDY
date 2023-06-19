def obter_vetor_origem(N1):
    return [N1, N1 + 1, N1 + 2]

def processar_vetor(vetor_origem):
    # Faça o processamento necessário no vetor de origem
    resultado = [valor * 2 for valor in vetor_origem]
    return resultado

N1 = int(input("Digite número origem:"))

vetor_origem = obter_vetor_origem(N1)

print("Elemento na posição 0:", vetor_origem[0])
print("Elemento na posição 2:", vetor_origem[2])

vetor_origem[2] = 73

print("Elemento na posição 1 após removeção", vetor_origem)

soma = 0
for elemento in vetor_origem:
    soma += elemento 
    
print("Soma de todos os elementos:", soma)

media = soma / len(vetor_origem)
print("Mèdia dos elementos", media)

dobro = [valor * 2 for valor in vetor_origem]
print("Os elementos dobrados:", dobro)