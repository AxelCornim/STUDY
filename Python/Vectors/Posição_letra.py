frase = "Olá, hello how you doing?"

if "how" in frase:
    print("A palabra 'how' está presente na frase.")
    posicao = frase.index('how')
    print("A posição do elemento 'how' é:", posicao)
else:
    print("A palavra 'how' não está pesente na frase.")