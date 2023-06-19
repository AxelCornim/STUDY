frase = "Olá, como você está?"

if "como" in frase:
    print("A palavra 'como' está presente na frase.")
    posicao = frase.index('como')
    print("A posição do elemento como é:", posicao)
else:
    print("A palavra 'como' não está presente na frase.")