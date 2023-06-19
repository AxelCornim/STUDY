def obter_elementos(num_elementos):
    elementos = []
    for i in range(1, num_elementos + 1):
        pergunta = f"Digite o {i}º elemento: "
        elemento = int(input(pergunta))
        elementos.append(elemento)
    return elementos

def encontrar_pares(elementos):
    valores_pares = []
    posicoes_pares = []
    for i, valor in enumerate(elementos):
        if valor % 2 == 0:
            valores_pares.append(valor)
            posicoes_pares.append(i)
    return valores_pares, posicoes_pares

num_elementos = int(input("Quantos elementos deseja colocar? "))
vetor = obter_elementos(num_elementos)
valores_pares, posicoes_pares = encontrar_pares(vetor)

print("Valores pares:", valores_pares)
print("Posições dos valores pares:", posicoes_pares)
