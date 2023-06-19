def obter_vetor_origem(N1):
    return [N1, N1 + 1, N1 + 2]

def processar_vetor(vetor_origem):
    # Faça o processamento necessário no vetor de origem
    resultado = [valor * 2 for valor in vetor_origem]
    return resultado

N1 = int(input("Digite número origem:"))

# Chame a função para obter o vetor de origem
vetor_origem = obter_vetor_origem(N1)

segundo_elemento = vetor_origem[1]
print("Segundo elemento:", segundo_elemento)

# Exiba o resultado
print("Vetor processado:", vetor_origem)

subvetor1 = vetor_origem[1:]
subvetor2 = vetor_origem[0:2]
subvetor3 = vetor_origem[-1:]

print()
print("Subvetor 1:", subvetor1)
print("Subvetor 2:", subvetor2)
print("Subvetor 3:", subvetor3)